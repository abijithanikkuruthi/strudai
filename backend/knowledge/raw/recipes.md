Note: This has been (partly) translated from https://tidalcycles.org/docs/patternlib/howtos/buildarpeggios

# Build Arpeggios

This page will teach you how to get started writing arpeggios using different techniques. It is a good way to learn Strudel in a more intuitive way.

## Arpeggios from notes

Start with a simple sequence of notes:

```strudel
note("c a f e").piano().slow(2)
```

Now, let's play one per cycle:

```strudel
note("<c a f e>").piano().slow(2)
```

On top of that, put a copy of the sequence, offset in time and pitch:

```strudel
"<c a f e>".off(1/8, add(7))
  .note().piano().slow(2)
```

Add some structure to the original sequence:

```strudel
"<c*2 a(3,8) f(3,8,2) e*2>"
  .off(1/8, add(7))
  .note().piano().slow(2)
```

Reverse in one speaker:

```strudel
"<c*2 a(3,8) f(3,8,2) e*2>"
  .off(1/8, add(7))
  .note().piano()
  .jux(rev).slow(2)
```

Let's add another layer:

```strudel
"<c*2 a(3,8) f(3,8,2) e*2>"
  .off(1/8, add(7))
  .off(1/8, add(12))
  .note().piano()
  .jux(rev).slow(2)
```

- added slow(2) to approximate tidals cps
- n was replaced with note, because using n does not work as note for samples
- legato 2 was removed because it does not work in combination with rev (bug)

## Arpeggios from chords

TODO


---

see https://strudel.cc/?zMEo5kowGrFc

# Microrhythms

Inspired by this [Mini-Lecture on Microrhythm Notation](https://www.youtube.com/watch?v=or7B6vI3jOo), let's look at how we can express microrhythms with Strudel.

The timestamps of the first rhythm are `0 1/5 1/2 2/3 1`. We could naively express this with a stack:

```strudel
s("hh").struct(
  stack(
    "x", // 0
    "~ x ~@3", // 1/5
    "~ x", // 1/2
    "~@2 x" // 2/3
))
```

While this works, it has two problems:

- it is not very compact
- the durations are wrong, e.g. the first note takes up the whole cycle

In the video, the duration of a timestamp is calculated by subtracting it from the next timestamp:

- 1/5 - 0 = 1/5 = 6/30
- 1/2 - 1/5 = 3/10 = 9/30
- 2/3 - 1/2 = 1/6 = 5/30
- 1 - 2/3 = 1/3 = 10/30

Using those, we can now express the rhythm much shorter:

```strudel
s("hh").struct("x@6 x@9 x@5 x@10")
```

The problems of the first notation are now fixed: it is much shorter and the durations are correct.
Still, this notation involved calculating the durations by hand, which could be automated:

```strudel
Pattern.prototype.micro = function (...timestamps) {
  const durations = timestamps.map((x, i, a) => {
    const next = i < a.length-1 ? a[i+1] : 1;
    return next - a[i]
  })
  return this.struct(timeCat(...durations.map(d => [d, 1]))).late(timestamps[0])
}
s('hh').micro(0, 1/5, 1/2, 2/3)
```

This notation is even shorter and it allows directly filling in the timestamps!

This is the second example of the video:

```strudel
Pattern.prototype.micro = function (...timestamps) {
  const durations = timestamps.map((x, i, a) => {
    const next = i < a.length-1 ? a[i+1] : 1;
    return next - a[i]
  })
  return this.struct(timeCat(...durations.map(d => [d, 1]))).late(timestamps[0])
}
s('hh').micro(0, 1/6, 2/5, 2/3, 3/4)
```

with bass: https://strudel.cc/?sTglgJJCPIeY


---

# Recipes

This page shows possible ways to achieve common (or not so common) musical goals.
There are often many ways to do a thing and there is no right or wrong.
The fun part is that each representation will give you different impulses when improvising.

## Arpeggios

An arpeggio is when the notes of a chord are played in sequence.
We can either write the notes by hand:

```strudel
note("c eb g c4")
.clip(2).s("gm_electric_guitar_clean")
```

...or use scales:

```strudel
n("0 2 4 7").scale("C:minor")
.clip(2).s("gm_electric_guitar_clean")
```

...or chord symbols:

```strudel
n("0 1 2 3").chord("Cm").mode("above:c3").voicing()
.clip(2).s("gm_electric_guitar_clean")
```

...using off:

```strudel
"0"
  .off(1/3, add(2))
  .off(1/2, add(4))
  .n()
  .scale("C:minor")
  .s("gm_electric_guitar_clean")
```

## Chopping Breaks

A sample can be looped and chopped like this:

```strudel
samples('github:yaxu/clean-breaks')
s("amen/4").fit().chop(32)
```

This fits the break into 8 cycles + chops it in 16 pieces.
The chops are not audible yet, because we're not doing any manipulation.
Let's add randmized doubling + reversing:

```strudel
samples('github:yaxu/clean-breaks')
s("amen/4").fit().chop(16).cut(1)
.sometimesBy(.5, ply("2"))
.sometimesBy(.25, mul(speed("-1")))
```

If we want to specify the order of samples, we can replace `chop` with `slice`:

```strudel
samples('github:yaxu/clean-breaks')
s("amen/4").fit()
  .slice(8, "<0 1 2 3 4*2 5 6 [6 7]>*2")
  .cut(1).rarely(ply("2"))
```

If we use `splice` instead of `slice`, the speed adjusts to the duration of the event:

```strudel
samples('github:yaxu/clean-breaks')
s("amen")
  .splice(8, "<0 1 2 3 4*2 5 6 [6 7]>*2")
  .cut(1).rarely(ply("2"))
```

Note that we don't need `fit`, because `splice` will do that by itself.

## Filter Envelopes

Using `lpenv`, we can make the filter move:

```strudel
note("g1 bb1 <c2 eb2> d2")
  .s("sawtooth")
  .lpf(400).lpenv(4)
  .scope()
```

The type of envelope depends on the methods you're setting. Let's set `lpa`:

```strudel
note("g1 bb1 <c2 eb2> d2")
  .s("sawtooth").lpq(8)
  .lpf(400).lpa(.2).lpenv(4)
  .scope()
```

Now the filter is attacking, rather than decaying as before (decay is the default). We can also do both

```strudel
note("g1 bb1 <c2 eb2> d2")
  .s("sawtooth").lpq(8)
  .lpf(400).lpa(.1).lpd(.1).lpenv(4)
  .scope()
```

You can play around with `lpa` | `lpd` | `lps` | `lpd` to see what the filter envelope will do.

## Layering Sounds

We can layer sounds by separating them with ",":

`note("<g1 bb1 d2 f1>")
.s("sawtooth, square") // <------
.scope()`

We can control the gain of individual sounds like this:

```strudel
note("<g1 bb1 d2 f1>")
.s("sawtooth, square:0:.5") // <--- "name:number:gain"
.scope()
```

For more control over each voice, we can use `layer`:

```strudel
note("<g1 bb1 d2 f1>").layer(
  x=>x.s("sawtooth").vib(4),
  x=>x.s("square").add(note(12))
).scope()
```

Here, we give the sawtooth a vibrato and the square is moved an octave up.
With `layer`, you can use any pattern method available on each voice, so sky is the limit..

## Oscillator Detune

We can fatten a sound by adding a detuned version to itself:

```strudel
note("<g1 bb1 d2 f1>")
.add(note("0,.1")) // <------ chorus
.s("sawtooth").scope()
```

Try out different values, or add another voice!

## Polyrhythms

Here is a simple example of a polyrhythm:

```strudel
s("bd*2,hh*3")
```

A polyrhythm is when 2 different tempos happen at the same time.

## Polymeter

This is a polymeter:

```strudel
s("<bd rim, hh hh oh>*4")
```

A polymeter is when 2 different bar lengths play at the same tempo.

## Phasing

This is a phasing:

```strudel
note("<C D G A Bb D C A G D Bb A>*[6,6.1]").piano()
```

Phasing happens when the same sequence plays at slightly different tempos.

## Running through samples

Using `run` with `n`, we can rush through a sample bank:

```strudel
samples('bubo:fox')
n(run(8)).s("ftabla")
```

This works great with sample banks that contain similar sounds, like in this case different recordings of a tabla.
Often times, you'll hear the beginning of the phrase not where the pattern begins.
In this case, I hear the beginning at the third sample, which can be accounted for with `early`.

```strudel
samples('bubo:fox')
n(run(8)).s("ftabla").early(2/8)
```

Let's add some randomness:

```strudel
samples('bubo:fox')
n(run(8)).s("ftabla").early(2/8)
.sometimes(mul(speed("1.5")))
```

## Tape Warble

We can emulate a pitch warbling effect like this:

```strudel
note("<c4 bb f eb>*8")
.add(note(perlin.range(0,.5))) // <------ warble
.clip(2).s("gm_electric_guitar_clean")
```

## Sound Duration

There are a number of ways to change the sound duration. Using clip:

```strudel
note("f ab bb c")
.clip("<2 1 .5 .25>")
```

The value of clip is relative to the duration of each event.
We can also create overlaps using release:

```strudel
note("f ab bb c")
.release("<2 1 .5 .25>")
```

This will smoothly fade out each sound for the given number of seconds.
We could also make the notes shorter by using a decay envelope:

```strudel
note("f ab bb c")
.decay("<2 1 .5 .25>")
```

When using samples, we also have `.end` to cut relative to the sample length:

```strudel
s("oh*4").end("<1 .5 .25 .1>")
```

Compare that to clip:

```strudel
s("oh*4").clip("<1 .5 .25 .1>")
```

or decay:

```strudel
s("oh*4").decay("<1 .5 .25 .1>")
```

## Wavetable Synthesis

You can loop a sample with `loop` / `loopEnd`:

```strudel
note("<c eb g f>").s("bd").loop(1).loopEnd(.05).gain(.2)
```

This allows us to play the first 5% of the bass drum as a synth!
To simplify loading wavetables, any sample that starts with `wt_` will be looped automatically:

```strudel
samples('github:bubobubobubobubo/dough-waveforms')
note("c eb g bb").s("wt_dbass").clip(2)
```

Running through different wavetables can also give interesting variations:

```strudel
samples('github:bubobubobubobubo/dough-waveforms')
note("c2*8").s("wt_dbass").n(run(8)).fast(2)
```

...adding a filter envelope + reverb:

```strudel
samples('github:bubobubobubobubo/dough-waveforms')
note("c2*8").s("wt_dbass").n(run(8))
.lpf(perlin.range(100,1000).slow(8))
.lpenv(-3).lpa(.1).room(.5).fast(2)
```


---

Note:

- this has been (partly) translated from https://tidalcycles.org/docs/patternlib/howtos/buildrhythms
- this only sounds good with `samples('github:tidalcycles/dirt-samples')` in prebake

# Build Rhythms

This page will teach you how to get started writing rhythms using different techniques. It is a good way to learn Strudel in a more intuitive way.

## From a simple to a complex rhythm

Simple bass drum - snare:

```strudel
s("bd sd").slow(2)
```

Let's pick a different snare sample:

```strudel
s("bd sd:3").slow(2)
```

Now, we are going to change the rhythm:

```strudel
s("bd*2 [~ sd:3]").slow(2)
```

And add some toms:

```strudel
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]").slow(2)
```

Start to transform, shift a quarter cycle every other cycle:

```strudel
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early(.25)).slow(2)
```

Pattern the shift amount:

```strudel
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early("<.25 .125 .5>")).slow(2)
```

Add some patterned effects:

```strudel
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early("<.25 .125 .5>"))
.shape("<0 .5 .3>")
.room(saw.range(0,.2).slow(4))
.slow(2)
```

More transformation:

```strudel
s("bd*2 [[~ lt] sd:3] lt:1 [ht mt*2]")
.every(2, early("<.25 .125 .5>"))
.shape("<0 .5 .3>")
.room(saw.range(0,.2).slow(4))
.jux(id, rev, x=>x.speed(2))
.slow(2)
```

## Another rhythmic construction

Let's start with a sequence:

```strudel
n("0 0 [2 0] [2 3]").s("feel").speed(1.5).slow(2)
```

We add a bit of flavour:

```strudel
n("0 <0 4> [2 0] [2 3]").s("feel").speed(1.5).slow(2)
```

Swap the samples round every other cycle:

TODO: implement `rot`
