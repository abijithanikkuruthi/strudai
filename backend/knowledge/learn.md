# Mini-notation

Just like [Tidal Cycles](https://tidalcycles.org/), Strudel uses a so called "Mini-Notation", which is a custom language that is designed for writing rhythmic patterns using little amounts of text.

## Note

This page just explains the entirety of the Mini-Notation syntax.
If you are just getting started with Strudel, you can learn the basics of the Mini-Notation in a more practical manner in the [workshop](/workshop/first-sounds).
After that, you can come back here if you want to understand every little detail.

## Example

Before diving deeper into the details, here is a flavour of how the Mini-Notation looks like:

```strudel
note(\`<
[e5 [b4 c5] d5 [c5 b4]]
[a4 [a4 c5] e5 [d5 c5]]
[b4 [~ c5] d5 e5]
[c5 a4 a4 ~]
[[~ d5] [~ f5] a5 [g5 f5]]
[e5 [~ c5] e5 [d5 c5]]
[b4 [b4 c5] d5 e5]
[c5 a4 a4 ~]
,
[[e2 e3]*4]
[[a2 a3]*4]
[[g#2 g#3]*2 [e2 e3]*2]
[a2 a3 a2 a3 a2 a3 b1 c2]
[[d2 d3]*4]
[[c2 c3]*4]
[[b1 b2]*2 [e2 e3]*2]
[[a1 a2]*4]
>\`)
```

## Mini Notation Format

The snippet above is enclosed in backticks (`), which allows you to write multi-line strings.

You can also use regular double quotes (`"`) for single line mini-notation, as we have done already.

If you do just want to get a regular string that is _not_ parsed as mini-notation, use single quotes (`'`).

## Sequences of events in a cycle

We can play more notes by separating them with spaces:

```strudel
note("c e g b")
```

Here, those four notes are squashed into one cycle, so each note is a quarter second long.
Try adding or removing notes and notice how the tempo changes!

```strudel
note("c d e f g a b")
```

Note that the overall duration of time does not change, and instead each note length decreases.
This is a key idea, as it illustrates the 'Cycle' in TidalCycles!

Each space-separated note in this sequence is an _event_.
The time duration of each event is based on the speed or tempo of the cycle, and how many events are present.
Taking the two examples above, we have four and eight events respectively, and since they have the same cycle duration, they each have to fit their events inside the same amount of time.

This is perhaps counter-intuitive if you are used to adding notes in a sequencer or piano roll and the overall length increasing.
But, it will begin to make sense as we go through more elements of mini-notation.

## Multiplication

A sequence can be sped up by multiplying it by a number using the asterisk symbol (`*`):

```strudel
note("[e5 b4 d5 c5]*2")
```

The multiplication by two here means that the sequence will play twice per cycle.

Multiplications can also be decimal (`*2.75`):

```strudel
note("[e5 b4 d5 c5]*2.75")
```

## Division

Contrary to multiplication, division can slow the sequence down by enclosing it in brackets and dividing it by a number (`/2`):

```strudel
note("[e5 b4 d5 c5]/2")
```

The division by two means that the sequence will be played over the course of two cycles.
You can also use decimal numbers for any tempo you like (`/2.75`).

```strudel
note("[e5 b4 d5 c5]/2.75")
```

## Angle Brackets

Using angle brackets `<>`, we can define the sequence length based on the number of events:

```strudel
note("<e5 b4 d5 c5>")
```

The above snippet is the same as:

```strudel
note("[e5 b4 d5 c5]/4")
```

The advantage of the angle brackets, is that we can add more events without needing to change the number at the end.

```strudel
note("<e5 b4 d5 c5 e5>")
```

```strudel
note("<e5 b4 d5 c5 e5 b4>")
```

This is more similar to traditional music sequencers and piano rolls, where adding a note increases the perceived overall duration.
We can also play a certain number of notes per cycle by using angle brackets with multiplication:

```strudel
note("<e5 b4 d5 c5 a4 c5>*8")
```

Now we are playing 8 notes per cycle!

## Subdividing time with bracket nesting

To create more interesting rhythms, you can _nest_ or _enclose_ sequences (put sequences inside sequences) with brackets `[]`, like this:

Compare the difference between the following:

```strudel
note("e5 b4 c5 d5 c5 b4")
```

```strudel
note("e5 [b4 c5] d5 c5 b4")
```

```strudel
note("e5 [b4 c5] d5 [c5 b4]")
```

```strudel
note("e5 [b4 c5] d5 [c5 b4 d5 e5]")
```

```strudel
note("e5 [b4 c5] d5 [c5 b4 [d5 e5]]")
```

What's going on here? When we nest/enclose multiple events inside brackets (`[]`), their duration becomes the length of one event in the outer sequence.

This is a very simple change to make, but it has profound consequences.
Remember what we said earlier about how the cycles in tidal stay the same length, and the individual event lengths are divided up in this cycle?
Well, what this means is that in TidalCycles, not only can you divide time any way you want, and you can also subdivide time any way you want!

## Rests

The "~" represents a rest, and will create silence between other events:

```strudel
note("[b4 [~ c5] d5 e5]")
```

Alternatively, "-" can be used instead of "~". It means the same thing.

## Parallel / polyphony

Using commas, we can play chords.
The following are the same:

```strudel
note("[g3,b3,e4]")
```

```strudel
note("g3,b3,e4")
```

But to play multiple chords in a sequence, we have to wrap them in brackets:

```strudel
note("<[g3,b3,e4] [a3,c3,e4] [b3,d3,f#4] [b3,e4,g4]>*2")
```

## Elongation

With the "@" symbol, we can specify temporal "weight" of a sequence child:

```strudel
note("<[g3,b3,e4]@2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

Here, the first chord has a weight of 2, making it twice the length of the other chords. The default weight is 1.

## Replication

Using "!" we can repeat without speeding up:

```strudel
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Randomness

Events with a "?" placed after them will have a 50% chance of being removed from the pattern:

```strudel
note("[g3,b3,e4]*8?")
```

Adding a number between 0 and 1 after the "?" will affect the likelihood of the event being removed. For example, events with "?0.1" placed after them will have a 10% chance of being removed:

```strudel
note("[g3,b3,e4]*8?0.1")
```

Events separated by a "|" will be chosen from at random:

`note("[g3,b3,e4] | [a3,c3,e4] | [b3,d3,f#4]")`

## Mini-notation review

To recap what we've learned so far, compare the following patterns:

```strudel
note("<g3 b3 e4 [a3,c3,e4] [b3,d3,f#4]>*2")
```

```strudel
note("<[g3,b3,e4] [a3,c3,e4] [b3,d3,f#4]>*2")
```

```strudel
note("<[g3,b3,e4]/2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

```strudel
note("<[g3,b3,e4]*2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

```strudel
note("<[g3,b3,e4] _ [a3,c3,e4] [b3,d3,f#4]>*2")
```

```strudel
note("<[g3,b3,e4]@2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

```strudel
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>*2")
```

```strudel
note("<[g3,b3,e4]? [a3,c3,e4] [b3,d3,f#4]>*2")
```

```strudel
note("<[g3|b3|e4] [a3,c3,e4] [b3,d3,f#4]>*2")
```

## Euclidian rhythms

Using round brackets after an event, we can create rhythmical sub-divisions based on three parameters: `beats`, `segments` and `offset`.
This algorithm can be found in many different types of music software, and is often referred to as a [Euclidean rhythm](https://en.wikipedia.org/wiki/Euclidean_rhythm) sequencer, after computer scientist Godfriend Toussaint.
Why is it interesting? Well, consider the following simple example:

`s("bd(3,8,0)")`

Sound familiar?
This is a popular Euclidian rhythm going by various names, such as "Pop Clave".
These rhythms can be found in all musical cultures, and the Euclidian rhythm algorithm allows us to express them extremely easily.
Writing this rhythm out in full require describing:

```strudel
s("bd ~ ~ bd ~ ~ bd ~")
```

But using the Euclidian rhythm notation, we only need to express "3 beats over 8 segments, starting on position 1".

This makes it easy to write patterns with interesting rhythmic structures and variations that still sound familiar:

```strudel
note("e5(2,8) b4(3,8) d5(2,8) c5(3,8)").slow(2)
```

Note that since the example above does not use the third `offset` parameter, it can be written simply as `"(3,8)"`.

```strudel
s("bd(3,8)")
```

Let's look at those three parameters in detail.

### Beats

`beats`: the first parameter controls how may beats will be played.
Compare these:

```strudel
s("bd(2,8)")
```

```strudel
s("bd(5,8)")
```

```strudel
s("bd(7,8)")
```

### Segments

`segments`: the second parameter controls the total amount of segments the beats will be distributed over:

```strudel
s("bd(3,4)")
```

```strudel
s("bd(3,8)")
```

```strudel
s("bd(3,13)")
```

### Offsets

`offset`: the third (optional) parameter controls the starting position for distributing the beats.
We need a secondary rhythm to hear the difference:

```strudel
s("bd(3,8,0), hh cp")
```

```strudel
s("bd(3,8,3), hh cp")
```

```strudel
s("bd(3,8,5), hh cp")
```

## Mini-notation exercise

The most fun thing about the mini-notation, is that everything you have just learned can be combined in various ways!

Starting with this one `n`, can you make a _pattern string_ that uses every single mini-notation element above?

```strudel
n("60")
```

<br />

Next: How do [Samples](/learn/samples) play into this?


---

# Sounds

We can play sounds with `s`, in two different ways:

- `s` can trigger audio samples, where a sound file is loaded in the background and played back:
  
```strudel
s("bd hh sd hh")
```

- `s` can trigger audio synthesisers, which are synthesised in real-time using code also running in the background:
  
```strudel
s("sawtooth square triangle sine")
```

You can learn more about both of these approaches in the pages [Synths](/learn/synths) and [Samples](/learn/samples).

# Combining notes and sounds

In both of the above cases, we are no longer directly controlling the `note`/`freq` of the sound heard via `s`, as we were in the [Notes](/workshop/first-notes/) page.

So how can we both control the sound and the pitch? We can _combine_ `note`/`freq` with `s` to change the sound of our pitches:

```strudel
note("a3 c#4 e4 a4").s("sawtooth")
```

```strudel
note("57 61 64 69").s("sine")
```

```strudel
freq("220 275 330 440").s("triangle")
```

The last example will actually sound the same with or without `s`, because `triangle` is the default value for `s`.

What about combining different notes with different sounds at the same time?

```strudel
freq("220 275 330 440 550").s("triangle sawtooth sine")
```

Hmm, something interesting is going on there, related to there being five notes and three sounds.

Let's now take a step back and think about the Strudel [Code](/learn/code/) we've been hearing so far.


---

# Notes

Pitches are an important building block in many musical traditions.
In Strudel, pitches can be expressed as note names, note numbers or frequencies.
Here's the same pattern written in three different ways:

- `note`: letter notation, good for those who are familiar with western music theory:

  
```strudel
note("a3 c#4 e4 a4")
```

- `note`: number notation, good for those who want to use recognisable pitches, but don't care about music theory:

  
```strudel
note("57 61 64 69")
```

- `freq`: frequency notation, good for those who want to go beyond standardised tuning systems:

  
```strudel
freq("220 275 330 440")
```

Let's look at those in more detail...

## `note` names

Notes names can be notated with the note letter, followed by the octave number. You can notate flats with `b` and sharps with `#`.

```strudel
note("a3 c#4 e4 a4")
```

By the way, you can edit the contents of the player, and press "update" to hear your change!
You can also press "play" on the next player without needing to stop the last one.

## `note` numbers

If you prefer, you can also use numbers with `note` instead:

```strudel
note("57 61 64 69")
```

These numbers are interpreted as so called [MIDI numbers](https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies), where adjacent whole numbers are one 'semitone' apart.

You could also write decimal numbers to get 'microtonal' pitches (in between the black and white piano notes):

```strudel
note("74.5 75 75.5 76")
```

## `freq`

To get maximum freedom, you can also use `freq` to directly control the frequency:

```strudel
freq("220 275 330 440")
```

## Hearing and frequency

In the above example, we play A3 (220Hz), C#4 natural (275Hz), E4 (330Hz) and A4 (440Hz), mirroring our previous examples.

But can you hear the difference between these individual frequencies?

```strudel
freq("220 221 223 224")
```

How about these?

```strudel
freq("2020 2021 2023 2024")
```

The higher we go up...

```strudel
freq("5020 5021 5023 5024")
```

The less distance we can hear between the frequencies!

```strudel
freq("10020 10021 10023 10024")
```

Why is this? [Human hearing operates logarithmically](https://www.audiocheck.net/soundtests_nonlinear.php).

## From notes to sounds

In this page, when we played a pattern of notes like this:

```strudel
note("a3 c#4 e4 a4")
```

We heard a simple synthesised sound, in fact we heard a [triangle wave oscillator](https://en.wikipedia.org/wiki/Triangle_wave).

This is the default synthesiser used by Strudel, but how do we then make different sounds in Strudel?

Let's find out in the next page on [Sounds](/learn/sounds).

<br />


---

# Audio Effects

Whether you're using a synth or a sample, you can apply any of the following built-in audio effects.
As you might suspect, the effects can be chained together, and they accept a pattern string as their argument.

# Signal chain

</img>

The signal chain in Strudel is as follows:

- An sound-generating event is triggered by a pattern
  - This has a start time and a duration, which is usually
    controlled by the note length and ADSR parameters
  - If we exceed the max polyphony, old sounds begin to die off
  - Muted sounds (one whose `s` value is `-`, `~`, or `_`) are skipped
- A sound is produced (through, say, a sample or an oscillator)
  - This is where detune-based effects (like `detune`, `penv`, etc. occur)
- The following will occur _in order_ and only if they've been called in the pattern. Note that all of these are
  single use effects, meaning that multiple occurrences of them in a pattern will simply override the values
  (e.g. you can't do `s("bd").lpf(100).distort(2).lpf(800)` to lowpass, distort, and then lowpass
  again)
  - Phase vocoder (`stretch`)
  - Gain is applied (`gain`)
    - This is where the main (volume) ADSR happens
  - A lowpass filter (`lpf`)
  - A highpass filter (`hpf`)
  - A bandpass filter (`bandpass`)
  - A vowel filter (`vowel`)
  - Sample rate reduction (`coarse`)
  - Bit crushing (`crush`)
  - Waveshape distortion (`shape`)
  - Normal distortion (`distort`)
  - Tremolo (`tremolo`)
  - Compressor (`compressor`)
  - Panning (`pan`)
  - Phaser (`phaser`)
  - Postgain (`post`)
- The sound is then split into multiple destinations
  - Dry output (amount controlled by `dry` parameter)
  - The sends
    - Analyzers
      - These are used for tooling like `scope` and `spectrum` and their setup usually happens behind the scenes
    - Delay (amount controlled by `delay` parameter)
    - Reverb (amount controlled by `room` parameter)
- The dry output, delay, and reverb are joined into what is called the "orbit" of the pattern (see more in the section below)
  - The `duck` effect affects the volume of all signals in the orbit
  - The orbit is then sent to the mixer

## Orbits

Orbits are the way in which outputs are handled in Strudel. They also prescribe which delay and reverb to associate with the dry signal.
By default, all orbits are mixed down to channels `1` and `2` in stereo, however with the "Multi Channel Orbits" setting
(under Settings at the right) you can use them as individual 2 channel stereo outs (orbit `i` will be mapped to
to channels `2i` and `2i + 1`). You can then use routers like Blackhole 16 to retrieve and record all of the channels in a DAW for later processing.

The default orbit is `1` and it is set with `orbit`. You may send a sound to multiple orbits via mininotation

```strudel
s("white").orbit("2,3,4").gain(0.2)
```

but please be careful as this will create three copies of the sound behind the scenes, meaning that if they are mixed
down to a single output, they will triple the volume. We've reduced the gain here to save your ears.

⚠️ There is only one delay and reverb per orbit, so please be aware that if you attempt to change the parameters on two
patterns pointing to the same orbit, it can lead to unpredictable results. Compare, for example, this pretty pluck
with a large reverb:

```strudel

$: s("triangle*4").decay(0.5).n(irand(12)).scale('C minor')
  .room(1).roomsize(10)
```

versus the same pluck with a muted kick drum coming in and overwriting the `roomsize` value:

```strudel

$: s("triangle*4").decay(0.5).n(irand(12)).scale('C minor')
  .room(1).roomsize(10)

$: s("bd\*4").room(0.01).roomsize(0.01).postgain(0)
```

This is due to them sharing the same orbit: the default of `1`. It can be corrected simply by updating the orbits to be
distinct:

```strudel

$: s("triangle*4").decay(0.5).n(irand(12)).scale('C minor')
  .room(1).roomsize(10).orbit(2)

$: s("bd\*4").room(0.01).roomsize(0.01).postgain(0)
```

## Continuous changes

As all of the above is triggered by a _sound occurring_, it is often the case that parameters may not be
modified continuously in time. For example,

```strudel

s("supersaw").lpf(tri.range(100, 5000).slow(2))
```

Will not produce a continually LFO'd low-pass filter due to the `tri` only being sampled every time the note hits
(in this case the default of once per cycle). You can fake it by introducing more sound-generating events, e.g.:

```strudel

s("supersaw").seg(16).lpf(tri.range(100, 5000).slow(2))
```

Some parameters _do_ induce continuous variations in time, though:

- The ADSR curve (governed by `attack`, `sustain`, `decay`, `release`)
- The pitch envelope curve (governed by `penv` and its associated ADSR)
- The FM curve (`fmenv`)
- The filter envelopes (`lpenv`, `hpenv`, `bpenv`)
- Tremolo (`tremolo`)
- Phaser (`phaser`)
- Vibrato (`vib`)
- Ducking (`duckorbit`)

# Filters

Filters are an essential building block of [subtractive synthesis](https://en.wikipedia.org/wiki/Subtractive_synthesis).
Strudel comes with 3 types of filters:

- low-pass filter: low frequencies may _pass_, high frequencies are cut off
- high-pass filter: high frequencies may _pass_, low frequencies are cut off
- band-pass filters: only a frequency band may _pass_, low and high frequencies around are cut off

Each filter has 2 parameters:

- cutoff: the frequency at which the filter starts to work. e.g. a low-pass filter with a cutoff of 1000Hz allows frequencies below 1000Hz to pass.
- q-value: Controls the resonance of the filter. Higher values sound more aggressive. Also see [Q-Factor](https://en.wikipedia.org/wiki/Q_factor)

## lpf

<JsDoc client:idle name="lpf" h={0} />

## lpq

<JsDoc client:idle name="lpq" h={0} />

## hpf

<JsDoc client:idle name="hpf" h={0} />

## hpq

<JsDoc client:idle name="hpq" h={0} />

## bpf

<JsDoc client:idle name="bpf" h={0} />

## bpq

<JsDoc client:idle name="bpq" h={0} />

## ftype

<JsDoc client:idle name="ftype" h={0} />

## vowel

<JsDoc client:idle name="vowel" h={0} />

# Amplitude Modulation

Amplitude modulation changes the amplitude (gain) periodically over time.

## am

<JsDoc client:idle name="am" h={0} />

## tremolosync

<JsDoc client:idle name="tremolosync" h={0} />

## tremolodepth

<JsDoc client:idle name="tremolodepth" h={0} />

## tremoloskew

<JsDoc client:idle name="tremoloskew" h={0} />

## tremolophase

<JsDoc client:idle name="tremolophase" h={0} />

## tremoloshape

<JsDoc client:idle name="tremoloshape" h={0} />

# Amplitude Envelope

The amplitude [envelope](<https://en.wikipedia.org/wiki/Envelope_(music)>) controls the dynamic contour of a sound.
Strudel uses ADSR envelopes, which are probably the most common way to describe an envelope:

![ADSR](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/ADSR_parameter.svg/1920px-ADSR_parameter.svg.png)

[image link](https://commons.wikimedia.org/wiki/File:ADSR_parameter.svg)

## attack

<JsDoc client:idle name="attack" h={0} />

## decay

<JsDoc client:idle name="decay" h={0} />

## sustain

<JsDoc client:idle name="sustain" h={0} />

## release

<JsDoc client:idle name="release" h={0} />

## adsr

<JsDoc client:idle name="adsr" h={0} />

# Filter Envelope

Each filter can receive an additional filter envelope controlling the cutoff value dynamically. It uses an ADSR envelope similar to the one used for amplitude. There is an additional parameter to control the depth of the filter modulation: `lpenv`|`hpenv`|`bpenv`. This allows you to play subtle or huge filter modulations just the same by only increasing or decreasing the depth.

`note("[c eb g <f bb>](3,8,<0 1>)".sub(12))
  .s("<sawtooth>/64")
  .lpf(sine.range(300,2000).slow(16))
  .lpa(0.005)
  .lpd(perlin.range(.02,.2))
  .lps(perlin.range(0,.5).slow(3))
  .lpq(sine.range(2,10).slow(32))
  .release(.5)
  .lpenv(perlin.range(1,8).slow(2))
  .ftype('24db')
  .room(1)
  .juxBy(.5,rev)
  .sometimes(add(note(12)))
  .stack(s("bd*2").bank('RolandTR909'))
  .gain(.5).fast(2)`

There is one filter envelope for each filter type and thus one set of envelope filter parameters preceded either by `lp`, `hp` or `bp`:

- `lpattack`, `lpdecay`, `lpsustain`, `lprelease`, `lpenv`: filter envelope for the lowpass filter.
  - alternatively: `lpa`, `lpd`, `lps`, `lpr` and `lpe`.
- `hpattack`, `hpdecay`, `hpsustain`, `hprelease`, `hpenv`: filter envelope for the highpass filter.
  - alternatively: `hpa`, `hpd`, `hps`, `hpr` and `hpe`.
- `bpattack`, `bpdecay`, `bpsustain`, `bprelease`, `bpenv`: filter envelope for the bandpass filter.
  - alternatively: `bpa`, `bpd`, `bps`, `bpr` and `bpe`.

## lpattack

<JsDoc client:idle name="lpattack" h={0} />

## lpdecay

<JsDoc client:idle name="lpdecay" h={0} />

## lpsustain

<JsDoc client:idle name="lpsustain" h={0} />

## lprelease

<JsDoc client:idle name="lprelease" h={0} />

## lpenv

<JsDoc client:idle name="lpenv" h={0} />

# Pitch Envelope

You can also control the pitch with envelopes!
Pitch envelopes can breathe life into static sounds:

```strudel
n("<-4,0 5 2 1>*<2!3 4>")
  .scale("<C F>/8:pentatonic")
  .s("gm_electric_guitar_jazz")
  .penv("<.5 0 7 -2>*2").vib("4:.1")
  .phaser(2).delay(.25).room(.3)
  .size(4).fast(1.5)
```

You also create some lovely chiptune-style sounds:

```strudel
n(run("<4 8>/16")).jux(rev)
.chord("<C^7 <Db^7 Fm7>>")
.dict('ireal')
.voicing().add(note("<0 1>/8"))
.dec(.1).room(.2)
.segment("<4 [2 8]>")
.penv("<0 <2 -2>>").patt(.02).fast(2)
```

Let's break down all pitch envelope controls:

## pattack

<JsDoc client:idle name="pattack" h={0} />

## pdecay

<JsDoc client:idle name="pdecay" h={0} />

## prelease

<JsDoc client:idle name="prelease" h={0} />

## penv

<JsDoc client:idle name="penv" h={0} />

## pcurve

<JsDoc client:idle name="pcurve" h={0} />

## panchor

<JsDoc client:idle name="panchor" h={0} />

# Dynamics

## gain

<JsDoc client:idle name="gain" h={0} />

## velocity

<JsDoc client:idle name="velocity" h={0} />

## compressor

<JsDoc client:idle name="compressor" h={0} />

## postgain

<JsDoc client:idle name="postgain" h={0} />

## xfade

<JsDoc client:idle name="xfade" h={0} />

# Panning

## jux

<JsDoc client:idle name="jux" h={0} />

## juxBy

<JsDoc client:idle name="juxBy" h={0} />

## pan

<JsDoc client:idle name="pan" h={0} />

# Waveshaping

## coarse

<JsDoc client:idle name="coarse" h={0} />

## crush

<JsDoc client:idle name="crush" h={0} />

## distort

<JsDoc client:idle name="distort" h={0} />

# Global Effects

## Local vs Global Effects

While the above listed "local" effects will always create a separate effects chain for each event,
global effects use the same chain for all events of the same orbit:

## orbit

<JsDoc client:idle name="orbit" h={0} />

## Delay

### delay

<JsDoc client:idle name="delay" h={0} />

### delaytime

<JsDoc client:idle name="delaytime" h={0} />

### delayfeedback

<JsDoc client:idle name="delayfeedback" h={0} />

## Reverb

### room

<JsDoc client:idle name="room" h={0} />

### roomsize

<JsDoc client:idle name="roomsize" h={0} />

### roomfade

<JsDoc client:idle name="roomfade" h={0} />

### roomlp

<JsDoc client:idle name="roomlp" h={0} />

### roomdim

<JsDoc client:idle name="roomdim" h={0} />

### iresponse

<JsDoc client:idle name="iresponse" h={0} />

## Phaser

### phaser

<JsDoc client:idle name="phaser" h={0} />

### phaserdepth

<JsDoc client:idle name="phaserdepth" h={0} />

### phasercenter

<JsDoc client:idle name="phasercenter" h={0} />

### phasersweep

<JsDoc client:idle name="phasersweep" h={0} />

## Duck

### duckorbit

<JsDoc client:idle name="duckorbit" h={0} />

### duckattack

<JsDoc client:idle name="duckattack" h={0} />

### duckdepth

<JsDoc client:idle name="duckdepth" h={0} />

Next, we'll look at input / output via [MIDI, OSC and other methods](/learn/input-output).


---

# Continuous Signals

Signals are patterns with continuous values, meaning they have theoretically infinite steps.
They can provide streams of numbers that can be sampled at discrete points in time.

## saw

<JsDoc client:idle name="saw" h={0} />

## sine

<JsDoc client:idle name="sine" h={0} />

## cosine

<JsDoc client:idle name="cosine" h={0} />

## tri

<JsDoc client:idle name="tri" h={0} />

## square

<JsDoc client:idle name="square" h={0} />

## rand

<JsDoc client:idle name="rand" h={0} />

## Ranges from -1 to 1

There is also `saw2`, `sine2`, `cosine2`, `tri2`, `square2` and `rand2` which have a range from -1 to 1!

## perlin

<JsDoc client:idle name="perlin" h={0} />

## irand

<JsDoc client:idle name="irand" h={0} />

## brand

<JsDoc client:idle name="brand" h={0} />

## brandBy

<JsDoc client:idle name="brandBy" h={0} />

## mouseX

<JsDoc client:idle name="mousex" h={0} />

## mouseY

<JsDoc client:idle name="mousey" h={0} />

Next up: [Random Modifiers](/learn/random-modifiers)


---

# Samples

Samples are the most common way to make sound with tidal and strudel.
A sample is a (commonly short) piece of audio that is used as a basis for sound generation, undergoing various transformations.
Music that is based on samples can be thought of as a collage of sound. [Read more about Sampling](<https://en.wikipedia.org/wiki/Sampling_(music)>)

Strudel allows loading samples in the form of audio files of various formats (wav, mp3, ogg) from any publicly available URL.

# Default Samples

By default, strudel comes with a built-in "sample map", providing a solid base to play with.

```strudel
s("bd sd [~ bd] sd,hh*16, misc")
```

Here, we are using the `s` function to play back different default samples (`bd`, `sd`, `hh` and `misc`) to get a drum beat.

For drum sounds, strudel uses the comprehensive [tidal-drum-machines](https://github.com/ritchse/tidal-drum-machines) library, with the following naming convention:

| Drum                 | Abbreviation |
| -------------------- | ------------ |
| Bass drum, Kick drum | bd           |
| Snare drum           | sd           |
| Rimshot              | rim          |
| Clap                 | cp           |
| Closed hi-hat        | hh           |
| Open hi-hat          | oh           |
| Crash                | cr           |
| Ride                 | rd           |
| High tom             | ht           |
| Medium tom           | mt           |
| Low tom              | lt           |

  original von Pbroks13

More percussive sounds:

| Source                              | Abbreviation |
| ----------------------------------- | ------------ |
| Shakers (and maracas, cabasas, etc) | sh           |
| Cowbell                             | cb           |
| Tambourine                          | tb           |
| Other percussions                   | perc         |
| Miscellaneous samples               | misc         |
| Effects                             | fx           |

Furthermore, strudel also loads instrument samples from [VCSL](https://github.com/sgossner/VCSL) by default.

To see which sample names are available, open the `sounds` tab in the [REPL](https://strudel.cc/).

You can also create custom aliases for existing sounds using the `soundAlias` function:

`soundAlias('RolandTR808_bd', 'kick')
s("kick")`

Note that only the sample maps (mapping names to URLs) are loaded initially, while the audio samples themselves are not loaded until they are actually played.
This behaviour of loading things only when they are needed is also called `lazy loading`.
While it saves resources, it can also lead to sounds not being audible the first time they are triggered, because the sound is still loading.
[This might be fixed in the future](https://codeberg.org/uzu/strudel/issues/187)

# Sound Banks

If we open the `sounds` tab and then `drum-machines`, we can see that the drum samples are all prefixed with drum machine names: `RolandTR808_bd`, `RolandTR808_sd`, `RolandTR808_hh` etc..

We _could_ use them like this:

```strudel
s("RolandTR808_bd RolandTR808_sd,RolandTR808_hh*16")
```

... but thats obviously a bit much to write. Using the `bank` function, we can shorten this to:

```strudel
s("bd sd,hh*16").bank("RolandTR808")
```

You could even pattern the bank to switch between different drum machines:

```strudel
s("bd sd,hh*16").bank("<RolandTR808 RolandTR909>")
```

Behind the scenes, `bank` will just prepend the drum machine name to the sample name with `_` to get the full name.
This of course only works because the name after `_` (`bd`, `sd` etc..) is standardized.
Also note that some banks won't have samples for all sounds!

# Selecting Sounds

If we open the `sounds` tab again, followed by tab `drum machines`, there is also a number behind each name, indicating how many individual samples are available.
For example `RolandTR909_hh(4)` means there are 4 samples of a TR909 hihat available.
By default, `s` will play the first sample, but we can select the other ones using `n`, starting from 0:

```strudel
s("hh*8").bank("RolandTR909").n("0 1 2 3")
```

Numbers that are too high will just wrap around to the beginning

```strudel
s("hh*8").bank("RolandTR909").n("0 1 2 3 4 5 6 7")
```

Here, 0-3 will play the same sounds as 4-7, because `RolandTR909_hh` only has 4 sounds.

Selecting sounds also works inside the mini notation, using "`:`" like this:

```strudel
s("bd*4,hh:0 hh:1 hh:2 hh:3 hh:4 hh:5 hh:6 hh:7")
.bank("RolandTR909")
```

# Loading Custom Samples

You can load a non-standard sample map using the `samples` function.

## Loading samples from file URLs

In this example we assign names `bassdrum`, `hihat` and `snaredrum` to specific audio files on a server:

```strudel
samples({
  bassdrum: 'bd/BT0AADA.wav',
  hihat: 'hh27/000_hh27closedhh.wav',
  snaredrum: ['sd/rytm-01-classic.wav', 'sd/rytm-00-hard.wav'],
}, 'https://raw.githubusercontent.com/tidalcycles/Dirt-Samples/master/');
 
s("bassdrum snaredrum:0 bassdrum snaredrum:1, hihat*16")
```

You can freely choose any combination of letters for each sample name. It is even possible to override the default sounds.
The names you pick will be made available in the `s` function.
Make sure that the URL and each sample path form a correct URL!

In the above example, `bassdrum` will load:

```
https://raw.githubusercontent.com/tidalcycles/Dirt-Samples/master/bd/BT0AADA.wav
|----------------------base path --------------------------------|--sample path-|
```

Note that we can either load a single file, like for `bassdrum` and `hihat`, or a list of files like for `snaredrum`!
As soon as you run the code, your chosen sample names will be listed in `sounds` -> `user`.

## Loading Samples from a strudel.json file

The above way to load samples might be tedious to write out / copy paste each time you write a new pattern.
To avoid that, you can simply pass a URL to a `strudel.json` file somewhere on the internet:

`samples('https://raw.githubusercontent.com/tidalcycles/Dirt-Samples/master/strudel.json')
s("bd sd bd sd,hh*16")`

The file is expected to define a sample map using JSON, in the same format as described above.
Additionally, the base path can be defined with the `_base` key.
The last section could be written as:

```json
{
  "_base": "https://raw.githubusercontent.com/tidalcycles/Dirt-Samples/master/",
  "bassdrum": "bd/BT0AADA.wav",
  "snaredrum": "sd/rytm-01-classic.wav",
  "hihat": "hh27/000_hh27closedhh.wav"
}
```

Please note that browsers will often cache `strudel.json` on first load, and keep using the cached
version even if the orginal has been updated. If this bites you (for example while developing a new
sample pack), you can force the browser to download a new copy by i.e. changing capitalization of one
character in the URL, or adding a URL attribute, such as:

```javascript
samples('https://raw.githubusercontent.com/tidalcycles/Dirt-Samples/master/strudel.json?version=2');
```

that gets ignored by GitHub (but changes the URL, forcing the browser to reload every time we increase
the version number).

It is also possible, of course, to just remove it from cache (deleting cache in browser Privacy settings,
or from the dev console if you're technically minded, or by using a cache deleting extension).

## Generating strudel.json

You can use [@strudel/sampler](https://www.npmjs.com/package/@strudel/sampler) to generate a strudel.json file for you, by running:

```sh
npx --yes @strudel/sampler --json > strudel.json
```

See other uses of strudel/sampler further below, under "From Disk via @strudel/sampler".

## Github Shortcut

Because loading samples from github is common, there is a shortcut:

```strudel
samples('github:tidalcycles/dirt-samples')
s("bd sd bd sd,hh*16")
```

The format is `samples('github:<user>/<repo>/<branch>')`. If you omit `branch` (like above), the `main` branch will be used.
It assumes a `strudel.json` file to be present at the root of the repository:

```
https://raw.githubusercontent.com/<user>/<repo>/<branch>/strudel.json
```

## From Disk via "Import Sounds Folder"

If you don't want to upload your samples to the internet, you can also load them from your local disk.
Go to the `sounds` tab in the REPL and open the `import-sounds` tab below the search bar.
Press the "import sounds folder" button and select a folder that contains audio files.
The folder you select can also contain subfolders with audio files.
Example:

```
└─ samples
   ├─ swoop
   │  ├─ swoopshort.wav
   │  ├─ swooplong.wav
   │  └─ swooptight.wav
   └─ smash
      ├─ smashhigh.wav
      ├─ smashlow.wav
      └─ smashmiddle.wav
```

In the above example the folder `samples` contains 2 subfolders `swoop` and `smash`, which contain audio files.
If you select that `samples` folder, the `user` tab (next to the `import-sounds` tab) will then contain 2 new sounds: `swoop(3) smash(3)`
The individual samples can the be played normally like `s("swoop:0 swoop:1 smash:2")`.
The samples within each sound use zero-based indexing in alphabetical order.

## From Disk via @strudel/sampler

Instead of loading your samples into your browser with the "import sounds folder" button, you can also serve the samples from a local file server.
The easiest way to do this is using [@strudel/sampler](https://www.npmjs.com/package/@strudel/sampler):

```sh
cd samples
npx @strudel/sampler
```

Then you can load it via:

```strudel
samples('http://localhost:5432/');
 
n("<0 1 2>").s("swoop smash")
```

The handy thing about `@strudel/sampler` is that it auto-generates the `strudel.json` file based on your folder structure.
You can see what it generated by going to `http://localhost:5432` with your browser.

Note: You need [NodeJS](https://nodejs.org/) installed on your system for this to work.

## Specifying Pitch

To make sure your samples are in tune when playing them with `note`, you can specify a base pitch like this:

```strudel
samples({
  'gtr': 'gtr/0001_cleanC.wav',
  'moog': { 'g3': 'moog/005_Mighty%20Moog%20G3.wav' },
}, 'github:tidalcycles/dirt-samples');
note("g3 [bb3 c4] <g4 f4 eb4 f3>@2").s("gtr,moog").clip(1)
  .gain(.5)
```

We can also declare different samples for different regions of the keyboard:

```strudel
setcpm(60)
samples({
  'moog': {
    'g2': 'moog/004_Mighty%20Moog%20G2.wav',
    'g3': 'moog/005_Mighty%20Moog%20G3.wav',
    'g4': 'moog/006_Mighty%20Moog%20G4.wav',
  }}, 'github:tidalcycles/dirt-samples')

note("g2!2 <bb2 c3>!2, <c4@3 [<eb4 bb3> g4 f4]>")
.s('moog').clip(1)
.gain(.5)
```

The sampler will always pick the closest matching sample for the current note!

Note that this notation for pitched sounds also works inside a `strudel.json` file.

## Shabda

If you don't want to select samples by hand, there is also the wonderful tool called [shabda](https://shabda.ndre.gr/).
With it, you can enter any sample name(s) to query from [freesound.org](https://freesound.org/). Example:

```strudel
samples('shabda:bass:4,hihat:4,rimshot:2')

$: n("0 1 2 3 0 1 2 3").s('bass')
$: n("0 1*2 2 3*2").s('hihat').clip(1)
$: n("~ 0 ~ 1 ~ 0 0 1").s('rimshot')
```

You can also generate artificial voice samples with any text, in multiple languages.
Note that the language code and the gender parameters are optional and default to `en-GB` and `f`

```strudel
samples('shabda/speech:the_drum,forever')
samples('shabda/speech/fr-FR/m:magnifique')

$: s("the_drum*2").chop(16).speed(rand.range(0.85,1.1))
$: s("forever magnifique").slow(4).late(0.125)
```

# Sampler Effects

Sampler effects are functions that can be used to change the behaviour of sample playback.

### begin

<JsDoc client:idle name="Pattern.begin" h={0} />

### end

<JsDoc client:idle name="Pattern.end" h={0} />

### loop

<JsDoc client:idle name="loop" h={0} />

### loopBegin

<JsDoc client:idle name="loopBegin" h={0} />

### loopEnd

<JsDoc client:idle name="loopEnd" h={0} />

### cut

<JsDoc client:idle name="cut" h={0} />

### clip

<JsDoc client:idle name="clip" h={0} />

### loopAt

<JsDoc client:idle name="Pattern.loopAt" h={0} />

### fit

<JsDoc client:idle name="fit" h={0} />

### chop

<JsDoc client:idle name="Pattern.chop" h={0} />

### striate

<JsDoc client:idle name="Pattern.striate" h={0} />

### slice

<JsDoc client:idle name="Pattern.slice" h={0} />

### splice

<JsDoc client:idle name="splice" h={0} />

### scrub

<JsDoc client:idle name="Pattern.scrub" h={0} />

### speed

<JsDoc client:idle name="speed" h={0} />

After samples, let's see what [Synths](/learn/synths) afford us.


---

# Synths

In addition to the sampling engine, strudel comes with a synthesizer to create sounds on the fly.

## Basic Waveforms

The basic waveforms are `sine`, `sawtooth`, `square` and `triangle`, which can be selected via `sound` (or `s`):

```strudel
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("<sawtooth square triangle sine>")
._scope()
```

If you don't set a `sound` but a `note` the default value for `sound` is `triangle`!

## Noise

You can also use noise as a source by setting the waveform to: `white`, `pink` or `brown`. These are different
flavours of noise, here written from hard to soft.

```strudel
sound("<white pink brown>")._scope()
```

Here's a more musical example of how to use noise for hihats:

```strudel
sound("bd*2,<white pink brown>*8")
.decay(.04).sustain(0)._scope()
```

Some amount of pink noise can also be added to any oscillator by using the `noise` paremeter:

```strudel
note("c3").noise("<0.1 0.25 0.5>")._scope()
```

You can also use the `crackle` type to play some subtle noise crackles. You can control noise amount by using the `density` parameter:

```strudel
s("crackle*4").density("<0.01 0.04 0.2 0.5>".slow(2))._scope()
```

### Additive Synthesis

Periodic waveforms are composed of several [harmonics](https://en.wikipedia.org/wiki/Harmonic) above a fundamental frequency, lying at integer multiples. These overtones combine to give a sound its unique timbral quality.

For the basic waveforms, we offer you control over these harmonics with the `partials` and `phases` functions.

#### Partials

`partials` refers to the magnitude of each harmonic relative to the fundamental frequency. They can thus be used to spectrally filter these waveforms and tame some of their harshness:

```strudel
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("sawtooth")
.partials([1, 1, "<1 0>", "<1 0>", "<1 0>", "<1 0>", "<1 0>"])
._scope()
```

`partials` can also be used to construct _new_ waveforms not present in our basic set with the 'user' sound source:

```strudel
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("user")
.partials([1, 0, 0.3, 0, 0.1, 0, 0, 0.3])
._scope()
```

We may algorithmically construct lists of magnitudes with Javascript code like:

```strudel
const numHarmonics = 22;
note("c2 <eb2 <g2 g1>>".fast(2))
.sound("saw")
.partials(new Array(numHarmonics).fill(1))
._scope()
```

which acts as a spectral filter. Or:

```strudel
note("c2 <eb2 <g2 g1>>").fast(2)
.sound("user")
.partials(new Array(50).fill(0)
  .map((_, idx) => ((-1) ** (idx + 1)) / (idx + 1))
)
._scope()
```

which recovers a familiar waveform.

`partials` is also compatible with pattern functions designed to produce lists, like `randL` or `binaryL`:

```strudel
note("c2 <eb2 <g2 g1>>").fast(2)
.sound("user")
.partials(randL(10))
._scope()
```

and with lists _of_ patterns:

```strudel
note("c2 <eb2 <g2 g1>>".fast(4))
.sound("user")
.partials([1, 0, "0 1", "0 1 0.3", rand])
._scope()
```

Note that the first value in the `partials` array controls the magnitude of the fundamental harmonic rather than the DC offset, which is fixed at 0.

#### Phases

Earlier, we mentioned that periodic waveforms can be broken into a set of harmonics above a fundamental frequency. Each harmonic has two defining properties: its magnitude (how loud it is) and its phase, which determines where in its cycle that sine wave starts when the waveform is built.

These phases too can be declared in Strudel and can give your sounds interesting depth.

```strudel
s("saw").seg(16).n(irand(12)).scale("F1:minor")
  .penv(48).panchor(0).pdec(0.05)
  .delay(0.25).room(0.25)
  .compressor(-20).vib(0.3)
  .partials(randL(200))
  .phases(randL(200))
```

## Vibrato

### vib

<JsDoc client:idle name="vib" h={0} />

### vibmod

<JsDoc client:idle name="vibmod" h={0} />

## FM Synthesis

FM Synthesis is a technique that changes the frequency of a basic waveform rapidly to alter the timbre.

You can use fm with any of the above waveforms, although the below examples all use the default triangle wave.

### fm

<JsDoc client:idle name="fm" h={0} />

### fmh

<JsDoc client:idle name="fmh" h={0} />

### fmattack

<JsDoc client:idle name="fmattack" h={0} />

### fmdecay

<JsDoc client:idle name="fmdecay" h={0} />

### fmsustain

<JsDoc client:idle name="fmsustain" h={0} />

### fmenv

<JsDoc client:idle name="fmenv" h={0} />

## Wavetable Synthesis

Strudel can also use the sampler to load custom waveforms as a replacement of the default waveforms used by WebAudio for the base synth. A default set of more than 1000 wavetables is accessible by default (coming from the [AKWF](https://www.adventurekid.se/akrt/waveforms/adventure-kid-waveforms/) set). You can also import/use your own. A wavetable is a one-cycle waveform, which is then repeated to create a sound at the desired frequency. It is a classic but very effective synthesis technique.

Any sample preceded by the `wt_` prefix will be loaded as a wavetable. This means that the `loop` argument will be set to `1` by default. You can scan over the wavetable by using `loopBegin` and `loopEnd` as well.

```strudel
samples('bubo:waveforms');
note("<[g3,b3,e4]!2 [a3,c3,e4] [b3,d3,f#4]>")
.n("<1 2 3 4 5 6 7 8 9 10>/2").room(0.5).size(0.9)
.s('wt_flute').velocity(0.25).often(n => n.ply(2))
.release(0.125).decay("<0.1 0.25 0.3 0.4>").sustain(0)
.cutoff(2000).cutoff("<1000 2000 4000>").fast(4)
._scope()

```

## ZZFX

The "Zuper Zmall Zound Zynth" [ZZFX](https://github.com/KilledByAPixel/ZzFX) is also integrated in strudel.
Developed by [Frank Force](https://frankforce.com/), it is a synth and FX engine originally intended to be used for size coding games.

It has 20 parameters in total, here is a snippet that uses all:

```strudel
note("c2 eb2 f2 g2") // also supports freq
  .s("{z_sawtooth z_tan z_noise z_sine z_square}%4")
  .zrand(0) // randomization
  // zzfx envelope
  .attack(0.001)
  .decay(0.1)
  .sustain(.8)
  .release(.1)
  // special zzfx params
  .curve(1) // waveshape 1-3
  .slide(0) // +/- pitch slide
  .deltaSlide(0) // +/- pitch slide (?)
  .noise(0) // make it dirty
  .zmod(0) // fm speed
  .zcrush(0) // bit crush 0 - 1
  .zdelay(0) // simple delay
  .pitchJump(0) // +/- pitch change after pitchJumpTime
  .pitchJumpTime(0) // >0 time after pitchJump is applied
  .lfo(0) // >0 resets slide + pitchJump + sets tremolo speed
  .tremolo(0.5) // 0-1 lfo volume modulation amount
  //.duration(.2) // overwrite strudel event duration
  //.gain(1) // change volume
  ._scope() // vizualise waveform (not zzfx related)

```

Note that you can also combine zzfx with all the other audio fx (next chapter).

Next up: [Audio Effects](/learn/effects)...


---

# Tonal Functions

These functions use [tonaljs](https://github.com/tonaljs/tonal) to provide helpers for musical operations.

### voicing()

<JsDoc client:idle name="voicing" h={0} />

Here's an example of how you can play chords and a bassline:

```strudel
chord("<C^7 A7b13 Dm7 G7>*2")
  .dict('ireal').layer(
  x=>x.struct("[~ x]*2").voicing()
  ,
  x=>n("0*4").set(x).mode("root:g2").voicing()
  .s('sawtooth').cutoff("800:4:2")
)
```

### scale(name)

<JsDoc client:idle name="scale" h={0} />

### transpose(semitones)

Transposes all notes to the given number of semitones:

```strudel
"[c2 c3]*4".transpose("<0 -2 5 3>").note()
```

This method gets really exciting when we use it with a pattern as above.

Instead of numbers, scientific interval notation can be used as well:

```strudel
"[c2 c3]*4".transpose("<1P -2M 4P 3m>").note()
```

### scaleTranspose(steps)

Transposes notes inside the scale by the number of steps:

```strudel
"[-8 [2,4,6]]*2"
.scale('C4 bebop major')
.scaleTranspose("<0 -1 -2 -3 -4 -5 -6 -4>*2")
.note()
```

### rootNotes(octave = 2)

Turns chord symbols into root notes of chords in given octave.

```strudel
"<C^7 A7b13 Dm7 G7>*2".rootNotes(3).note()
```

Together with layer, struct and voicings, this can be used to create a basic backing track:

```strudel
"<C^7 A7b13 Dm7 G7>*2".layer(
  x => x.voicings('lefthand').struct("[~ x]*2").note(),
  x => x.rootNotes(2).note().s('sawtooth').cutoff(800)
)
```


---

# Time Modifiers

The following functions modify a pattern temporal structure in some way.
Some of these have equivalent operators in the Mini Notation:

| function               | mini         |
| ---------------------- | ------------ |
| `"x".slow(2)`          | `"x/2"`      |
| `"x".fast(2)`          | `"x*2"`      |
| `"x".euclid(3,8)`      | `"x(3,8)"`   |
| `"x".euclidRot(3,8,1)` | `"x(3,8,1)"` |

## slow

<JsDoc client:idle name="Pattern.slow" h={0} />

## fast

<JsDoc client:idle name="Pattern.fast" h={0} />

## early

<JsDoc client:idle name="Pattern.early" h={0} />

## late

<JsDoc client:idle name="Pattern.late" h={0} />

## clip / legato

<JsDoc client:idle name="clip" h={0} />

## euclid

<JsDoc client:idle name="Pattern.euclid" h={0} />

### euclidRot

<JsDoc client:idle name="Pattern.euclidRot" h={0} />

### euclidLegato

<JsDoc client:idle name="Pattern.euclidLegato" h={0} />

## rev

<JsDoc client:idle name="Pattern.rev" h={0} />

## palindrome

<JsDoc client:idle name="palindrome" h={0} />

## iter

<JsDoc client:idle name="Pattern.iter" h={0} />

### iterBack

<JsDoc client:idle name="Pattern.iterBack" h={0} />

## ply

<JsDoc client:idle name="ply" h={0} />

## segment

<JsDoc client:idle name="segment" h={0} />

## compress

<JsDoc client:idle name="compress" h={0} />

## zoom

<JsDoc client:idle name="zoom" h={0} />

## linger

<JsDoc client:idle name="linger" h={0} />

## fastGap

<JsDoc client:idle name="fastGap" h={0} />

## inside

<JsDoc client:idle name="inside" h={0} />

## outside

<JsDoc client:idle name="outside" h={0} />

## cpm

<JsDoc client:idle name="cpm" h={0} />

## ribbon

<JsDoc client:idle name="ribbon" h={0} />

## swingBy

<JsDoc client:idle name="swingBy" h={0} />

## swing

<JsDoc client:idle name="swing" h={0} />

Apart from modifying time, there are ways to [Control Parameters](/functions/value-modifiers/).


---

# Random Modifiers

These methods add random behavior to your Patterns.

## choose

<JsDoc client:idle name="choose" h={0} />

## wchoose

<JsDoc client:idle name="wchoose" h={0} />

## chooseCycles

<JsDoc client:idle name="chooseCycles" h={0} />

## wchooseCycles

<JsDoc client:idle name="wchooseCycles" h={0} />

## degradeBy

<JsDoc client:idle name="Pattern.degradeBy" h={0} />

## degrade

<JsDoc client:idle name="Pattern.degrade" h={0} />

## undegradeBy

<JsDoc client:idle name="Pattern.undegradeBy" h={0} />

## undegrade

<JsDoc client:idle name="Pattern.undegrade" h={0} />

## sometimesBy

<JsDoc client:idle name="Pattern.sometimesBy" h={0} />

## sometimes

<JsDoc client:idle name="Pattern.sometimes" h={0} />

## someCyclesBy

<JsDoc client:idle name="Pattern.someCyclesBy" h={0} />

## someCycles

<JsDoc client:idle name="Pattern.someCycles" h={0} />

## often

<JsDoc client:idle name="Pattern.often" h={0} />

## rarely

<JsDoc client:idle name="Pattern.rarely" h={0} />

## almostNever

<JsDoc client:idle name="Pattern.almostNever" h={0} />

## almostAlways

<JsDoc client:idle name="Pattern.almostAlways" h={0} />

## never

<JsDoc client:idle name="Pattern.never" h={0} />

## always

<JsDoc client:idle name="Pattern.always" h={0} />

Next up: [Conditional Modifiers](/learn/conditional-modifiers)


---

# Conditional Modifiers

## lastOf

<JsDoc client:idle name="Pattern.lastOf" h={0} />

## firstOf

<JsDoc client:idle name="Pattern.firstOf" h={0} />

## when

<JsDoc client:idle name="Pattern.when" h={0} />

## chunk

<JsDoc client:idle name="Pattern.chunk" h={0} />

### chunkBack

<JsDoc client:idle name="Pattern.chunkBack" h={0} />

### fastChunk

<JsDoc client:idle name="Pattern.fastChunk" h={0} />

## arp

<JsDoc client:idle name="arp" h={0} />

## arpWith 🧪

<JsDoc client:idle name="arpWith" h={0} />

## struct

<JsDoc client:idle name="Pattern#struct" h={0} />

## mask

<JsDoc client:idle name="Pattern#mask" h={0} />

## reset

<JsDoc client:idle name="Pattern#reset" h={0} />

## restart

<JsDoc client:idle name="Pattern#restart" h={0} />

## hush

<JsDoc client:idle name="Pattern#hush" h={0} />

## invert

<JsDoc client:idle name="invert" h={0} />

## pick

<JsDoc client:idle name="pick" h={0} />

## pickmod

<JsDoc client:idle name="pickmod" h={0} />

## pickF

<JsDoc client:idle name="pickF" h={0} />

## pickmodF

<JsDoc client:idle name="pickmodF" h={0} />

## pickRestart

<JsDoc client:idle name="pickRestart" h={0} />

## pickmodRestart

<JsDoc client:idle name="pickmodRestart" h={0} />

## pickReset

<JsDoc client:idle name="pickReset" h={0} />

## pickmodReset

<JsDoc client:idle name="pickmodReset" h={0} />

## inhabit

<JsDoc client:idle name="inhabit" h={0} />

## inhabitmod

<JsDoc client:idle name="inhabitmod" h={0} />

## squeeze

<JsDoc client:idle name="squeeze" h={0} />

After Conditional Modifiers, let's see what [Accumulation Modifiers](/learn/accumulation) have to offer.


---

# Stepwise patterning (experimental)

This is a developing area of strudel, and behaviour might change or be renamed in future versions. Feedback and ideas are welcome!

## Introduction

Usually in strudel, the only reference point for most pattern transformations is the _cycle_. Now it is possible to also work with _steps_, via a growing range of functions.

For example usually when you `fastcat` two patterns together, the cycles will be squashed into half a cycle each:

```strudel
fastcat("bd hh hh", "bd hh hh cp hh").sound()
```

With the new stepwise `stepcat` function, the steps of the two patterns will be evenly distributed across the cycle:

```strudel
stepcat("bd hh hh", "bd hh hh cp hh").sound()
```

By default, steps are counted according to the 'top level' in mini-notation. For example `"a [b c] d e"` has five events in it per cycle, but is counted as four steps, where `[b c]` is counted as a single step.

However, you can mark a different metrical level to count steps relative to, using a `^` at the start of a sub-pattern. If we do this to the subpattern in our example: `"a [^b c] d e"`, then the pattern is now counted as having _eight_ steps. This is because 'b' and 'c' are each counted as single steps, and the events in the pattern are twice as long, and so counted as two steps each.

## Pacing the steps

Some stepwise functions don't appear to do very much on their own, for example these two examples of the `expand` function sound exactly the same despite being expanded by different amounts:

```strudel
"c a f e".expand(2).note().sound("folkharp")
```

```strudel
"c a f e".expand(4).note().sound("folkharp")
```

The number of steps per cycle is being changed behind the scenes, but on its own, that doesn't do anything. You will hear a difference however, once you use another stepwise function with it, for example `stepcat`:

```strudel
stepcat("c a f e".expand(2), "g d").note()
  .sound("folkharp")
```

```strudel
stepcat("c a f e".expand(4), "g d").note()
  .sound("folkharp")
```

You should be able to hear that `expand` increases the duration of the steps of the first subpattern, proportionally to the second one.

You can also change the speed of a pattern to match a given number of steps per cycle, with the `pace` function:

```strudel
stepcat("c a f e".expand(2), "g d").note()
  .sound("folkharp")
  .pace(8)
```

```strudel
stepcat("c a f e".expand(4), "g d").note()
  .sound("folkharp")
  .pace(8)
```

The first example has ten steps, and the second example has 18 steps, but are then both played a rate of 8 steps per cycle.

The argument to `expand` can also be patterned, and will be treated in a stepwise fashion. This means that the patterns from the changing values in the argument will be `stepcat`ted together:

```strudel
note("c a f e").sound("folkharp").expand("3 2 1 1 2 3")
```

This results in a dense pattern, because the different expanded versions are squashed into a single cycle. `pace` is again handy here for slowing down the pattern to a particular number of steps per cycle:

```strudel
note("c a f e").sound("folkharp").expand("3 2 1 1 2 3").pace(8)
```

Earlier versions of many of these functions had `s_` prefixes, and the `pace` function was previously known as `steps`. These still exist as aliases, but may have changed behaviour and will soon be removed. Please update your patterns!

## Stepwise functions

### pace

<JsDoc client:idle name="pace" h={0} />

### stepcat

<JsDoc client:idle name="stepcat" h={0} />

### stepalt

<JsDoc client:idle name="stepalt" h={0} />

### expand

<JsDoc client:idle name="expand" h={0} />

### contract

<JsDoc client:idle name="contract" h={0} />

### extend

<JsDoc client:idle name="extend" h={0} />

### take

<JsDoc client:idle name="take" h={0} />

### drop

<JsDoc client:idle name="drop" h={0} />

### polymeter

<JsDoc client:idle name="polymeter" h={0} />

### shrink

<JsDoc client:idle name="shrink" h={0} />

### grow

<JsDoc client:idle name="grow" h={0} />

### tour

<JsDoc client:idle name="tour" h={0} />

### zip

<JsDoc client:idle name="zip" h={0} />


---

# Creating Patterns

The following functions will return a pattern.
These are the equivalents used by the Mini Notation:

| function                       | mini             |
| ------------------------------ | ---------------- |
| `cat(x, y)`                    | `"<x y>"`        |
| `seq(x, y)`                    | `"x y"`          |
| `stack(x, y)`                  | `"x,y"`          |
| `stepcat([3,x],[2,y])`         | `"x@3 y@2"`      |
| `polymeter([a, b, c], [x, y])` | `"{a b c, x y}"` |
| `polymeterSteps(2, x, y, z)`   | `"{x y z}%2"`    |
| `silence`                      | `"~"`            |

## cat

<JsDoc client:idle name="cat" h={0} />

## seq

<JsDoc client:idle name="seq" h={0} />

## stack

<JsDoc client:idle name="stack" h={0} />

## stepcat

<JsDoc client:idle name="stepcat" h={0} />

## arrange

<JsDoc client:idle name="arrange" h={0} />

## polymeter

<JsDoc client:idle name="polymeter" h={0} />

## polymeterSteps

<JsDoc client:idle name="polymeterSteps" h={0} />

## silence

<JsDoc client:idle name="silence" h={0} />

## run

<JsDoc client:idle name="run" h={0} />

## binary

<JsDoc client:idle name="binary" h={0} />

## binaryN

<JsDoc client:idle name="binaryN" h={0} />

After Pattern Constructors, let's see what [Time Modifiers](/learn/time-modifiers) are available.


---

# Coding Syntax

Let's take a step back and understand how the syntax in Strudel works.

Take a look at this simple example:

```strudel
note("c a f e").s("piano")
```

- We have a word `note` which is followed by some brackets `()` with some words/letters/numbers inside, surrounded by quotes `"c a f e"`
- Then we have a dot `.` followed by another similar piece of code `s("piano")`.
- We can also see these texts are _highlighted_ using colours: word `note` is purple, the brackets `()` are grey, and the content inside the `""` are green. (The colors could be different if you've changed the default theme)

What happens if we try to 'break' this pattern in different ways?

```strudel
note(c a f e).s(piano)
```

```strudel
note("c a f e")s("piano")
```

```strudel
note["c a f e"].s{"piano"}
```

Ok, none of these seem to work...

```strudel
s("piano").note("c a f e")
```

This one does work, but now we only hear the first note...

So what is going on here?

# Functions, arguments and chaining

So far, we've seen the following syntax:

```
xxx("foo").yyy("bar")
```

Generally, `xxx` and `yyy` are called [_functions_](<https://en.wikipedia.org/wiki/Function_(computer_programming)>), while `foo` and `bar` are called function [_arguments_ or _parameters_](<https://en.wikipedia.org/wiki/Parameter_(computer_programming)>).
So far, we've used the functions to declare which aspect of the sound we want to control, and their arguments for the actual data.
The `yyy` function is called a [_chained_ function](https://en.wikipedia.org/wiki/Method_chaining), because it is preceded with a dot (`.`).

Generally, the idea with chaining is that code such as `a("this").b("that").c("other")` allows `a`, `b` and `c` functions to happen in a specified order, without needing to write them as three separate lines of code.
You can think of this as being similar to chaining audio effects together using guitar pedals or digital audio effects.

Strudel makes heavy use of chained functions. Here is a more sophisticated example:

```strudel
note("a3 c#4 e4 a4")
.s("sawtooth")
.cutoff(500)
//.delay(0.5)
.room(0.5)
```

## Write your own chained function

You can write your own chained function using `register`. Here's the above chain but registered as a reusable, chained function.

```strudel
const effectChain = register('effectChain', (pat) => pat
    .s("sawtooth")
    .cutoff(500)
    //.delay(0.5)
    .room(0.5)
  )
note("a3 c#4 e4 a4").effectChain()
```

Try adding `.rev()` after `effectChain()` to hear further effects added.

# Comments

The `//` in the example above is a line comment, resulting in the `delay` function being ignored.
It is a handy way to quickly turn code on and off.
Try uncommenting this line by deleting `//` and refreshing the pattern.
You can also use the keyboard shortcut `cmd-/` to toggle comments on and off.

You might noticed that some comments in the REPL samples include some words starting with a "@", like `@by` or `@license`.
Those are just a convention to define some information about the music. We will talk about it in the [Music metadata](/learn/metadata) section.

# Strings

Ok, so what about the content inside the quotes (e.g. `"c a f e"`)?
In JavaScript, as in most programming languages, this content is referred to as being a [_string_](<https://en.wikipedia.org/wiki/String_(computer_science)>).
A string is simply a sequence of individual characters.
In TidalCycles, double quoted strings are used to write _patterns_ using the mini-notation, and you may hear the phrase _pattern string_ from time to time.
If you want to create a regular string and not a pattern, you can use single quotes, e.g. `'C minor'` will not be parsed as Mini Notation.

The good news is, that this covers most of the JavaScript syntax needed for Strudel!

<br />


---

# Visual Feedback

There are several function that add visual feedback to your patterns.

## Mini Notation Highlighting

When you write mini notation with "double quotes" or \`backticks\`, the active parts of the mini notation will be highlighted:

```strudel
n("<0 2 1 3 2>*8")
.scale("<A1 D2>/4:minor:pentatonic")
.s("supersaw").lpf(300).lpenv("<4 3 2>\*4")
```

You can change the color as well, even pattern it:

```strudel
n("<0 2 1 3 2>*8")
.scale("<A1 D2>/4:minor:pentatonic")
.s("supersaw").lpf(300).lpenv("<4 3 2>*4")
.color("cyan magenta")
```

## Global vs Inline Visuals

The following functions all come with in 2 variants.

**Without prefix**: renders the visual to the background of the page:

```strudel
note("c a f e").color("white").punchcard()
```

**With `_` prefix**: renders the visual inside the code. Allows for multiple visuals

```strudel
note("c a f e").color("white")._punchcard()
```

Here we see the 2 variants for `punchcard`. The same goes for all others below.
To improve readability the following demos will all use the inline variant.

## Punchcard / Pianoroll

These 2 functions render a pianoroll style visual.
The only difference between the 2 is that `pianoroll` will render the pattern directly,
while `punchcard` will also take the transformations into account that occur afterwards:

```strudel
note("c a f e").color("white")
._punchcard()
.color("cyan")
```

Here, the `color` is still visible in the visual, even if it is applied after `_punchcard`.
On the contrary, the color is not visible when using `_pianoroll`:

```strudel
note("c a f e").color("white")
._pianoroll()
.color("cyan")
```

<br />

`punchcard` is less resource intensive because it uses the same data as used for the mini notation highlighting.

The visual can be customized by passing options. Those options are the same for both functions.

What follows is the API doc of all the options you can pass:

<JsDoc client:idle name="pianoroll" h={0} />

## Spiral

<JsDoc client:idle name="spiral" h={0} />

## Scope

<JsDoc client:idle name="scope" h={0} />

## Pitchwheel

<JsDoc client:idle name="pitchwheel" h={0} />

## Spectrum

<JsDoc client:idle name="spectrum" h={0} />

## markcss

<JsDoc client:idle name="markcss" h={0} />


---

# Colors

<Colors />


---

# MIDI, OSC and MQTT

Normally, Strudel is used to pattern sound, using its own '[web audio](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)'-based synthesiser called [SuperDough](https://codeberg.org/uzu/strudel/src/branch/main/packages/superdough).

It is also possible to pattern other things with Strudel, such as software and hardware synthesisers with MIDI, other software using Open Sound Control/OSC (including the [SuperDirt](https://github.com/musikinformatik/SuperDirt/) synthesiser commonly used with Strudel's sibling [TidalCycles](https://tidalcycles.org/)), or the MQTT 'internet of things' protocol.

# MIDI

Strudel supports MIDI without any additional software (thanks to [webmidi](https://npmjs.com/package/webmidi)), just by adding methods to your pattern:

## midin(inputName?)

<JsDoc client:idle name="midin" h={0} />

## midikeys(inputName?)

<JsDoc client:idle name="midikeys" h={0} />

## midi(outputName?,options?)

Either connect a midi device or use the IAC Driver (Mac) or Midi Through Port (Linux) for internal midi messages.
If no outputName is given, it uses the first midi output it finds.

```strudel

$: chord("<C^7 A7 Dm7 G7>").voicing().midi('IAC Driver')

```

In the console, you will see a log of the available MIDI devices as soon as you run the code,
e.g.

```
 `Midi connected! Using "Midi Through Port-0".`
```

The `.midi()` function accepts an options object with the following properties:

```strudel
$: note("d e c a f").midi('IAC Driver', { isController: true, midimap: 'default'})

```

<details>
<summary>Available Options</summary>

| Option       | Type          | Default   | Description                                                            |
| ------------ | ------------- | --------- | ---------------------------------------------------------------------- |
| isController | boolean       | false     | When true, disables sending note messages. Useful for MIDI controllers |
| latencyMs    | number        | 34        | Latency in milliseconds to align MIDI with audio engine                |
| noteOffsetMs | number        | 10        | Offset in milliseconds for note-off messages to prevent glitching      |
| midichannel  | number        | 1         | Default MIDI channel (1-16)                                            |
| velocity     | number        | 0.9       | Default note velocity (0-1)                                            |
| gain         | number        | 1         | Default gain multiplier for velocity (0-1)                             |
| midimap      | string        | 'default' | Name of MIDI mapping to use for control changes                        |
| midiport     | string/number | -         | MIDI device name or index                                              |

</details>

### midiport(outputName)

Selects the MIDI output device to use, pattern can be used to switch between devices.

```javascript
$: midiport('IAC Driver');
$: note('c a f e').midiport('<0 1 2 3>').midi();
```

<JsDoc client:idle name="midiport" h={0} />

## midichan(number)

Selects the MIDI channel to use. If not used, `.midi` will use channel 1 by default.

## midicmd(command)

`midicmd` sends MIDI system real-time messages to control timing and transport on MIDI devices.

It supports the following commands:

- `clock`/`midiClock` - Sends MIDI timing clock messages
- `start` - Sends MIDI start message
- `stop` - Sends MIDI stop message
- `continue` - Sends MIDI continue message

// You can control the clock with a pattern and ensure it starts in sync when the repl begins.
// Note: It might act unexpectedly if MIDI isn't set up initially.

`$:stack(
  midicmd("clock*48,<start stop>/2").midi('IAC Driver')
)`

## control, ccn && ccv

- `control` sends MIDI control change messages to your MIDI device.
- `ccn` sets the cc number. Depends on your synths midi mapping
- `ccv` sets the cc value. normalized from 0 to 1.

```strudel
note("c a f e").control([74, sine.slow(4)]).midi()
```

```strudel
note("c a f e").ccn(74).ccv(sine.slow(4)).midi()
```

In the above snippet, `ccn` is set to 74, which is the filter cutoff for many synths. `ccv` is controlled by a saw pattern.
Having everything in one pattern, the `ccv` pattern will be aligned to the note pattern, because the structure comes from the left by default.
But you can also control cc messages separately like this:

```strudel
$: note("c a f e").midi()
$: ccv(sine.segment(16).slow(4)).ccn(74).midi()
```

Instead of setting `ccn` and `ccv` directly, you can also create mappings with `midimaps`:

## midimaps

<JsDoc client:idle name="midimaps" h={0} />

## defaultmidimap

<JsDoc client:idle name="defaultmidimap" h={0} />

## progNum (Program Change)

`progNum` sends MIDI program change messages to switch between different presets/patches on your MIDI device.
Program change values should be numbers between 0 and 127.

```strudel
// Switch between programs 0 and 1 every cycle
progNum("<0 1>").midi()

// Play notes while changing programs
note("c3 e3 g3").progNum("<0 1 2>").midi()
```

Program change messages are useful for switching between different instrument sounds or presets during a performance.
The exact sound that each program number maps to depends on your MIDI device's configuration.

## sysex, sysexid && sysexdata (System Exclusive Message)

`sysex` sends MIDI System Exclusive (SysEx) messages to your MIDI device.
ysEx messages are device-specific commands that allow deeper control over synthesizer parameters.
The value should be an array of numbers between 0-255 representing the SysEx data bytes.

```strudel
// Send a simple SysEx message
let id = 0x43; //Yamaha
//let id = "0x00:0x20:0x32"; //Behringer ID can be an array of numbers
let data = "0x79:0x09:0x11:0x0A:0x00:0x00"; // Set NSX-39 voice to say "Aa"
$: note("c a f e").sysex(id, data).midi();
$: note("c a f e").sysexid(id).sysexdata(data).midi();
```

The exact format of SysEx messages depends on your MIDI device's specification.
Consult your device's MIDI implementation guide for details on supported SysEx messages.

## midibend && miditouch

`midibend` sets MIDI pitch bend (-1 - 1)
`miditouch` sets MIDI key after touch (0-1)

```strudel
note("c a f e").midibend(sine.slow(4).range(-0.4,0.4)).midi()
```

```strudel
note("c a f e").miditouch(sine.slow(4).range(0,1)).midi()
```

# OSC/SuperDirt/StrudelDirt

In TidalCycles, sound is usually generated using [SuperDirt](https://github.com/musikinformatik/SuperDirt/), which runs inside SuperCollider. Strudel also supports using SuperDirt, although it requires installing some additional software.

There is also [StrudelDirt](https://github.com/daslyfe/StrudelDirt) which is SuperDirt with some optimisations for working with Strudel. (A longer term aim is to merge these optimisations back into mainline SuperDirt)

## Prequisites

To get SuperDirt to work with Strudel, you need to

1. install SuperCollider + sc3 plugins, see [Tidal Docs](https://tidalcycles.org/docs/) (Install Tidal) for more info.
2. install SuperDirt, or the [StrudelDirt](https://github.com/daslyfe/StrudelDirt) fork which is optimised for use with Strudel
3. install [node.js](https://nodejs.org/en/)
4. download [Strudel Repo](https://codeberg.org/uzu/strudel/) (or git clone, if you have git installed)
5. run `pnpm i` in the strudel directory
6. run `pnpm run osc` to start the osc server, which forwards OSC messages from Strudel REPL to SuperCollider

Now you're all set!

## Usage

1. Start SuperCollider, either using SuperCollider IDE or by running `sclang` in a terminal
2. Open the [Strudel REPL](https://strudel.cc/#cygiYmQgc2QiKS5vc2MoKQ%3D%3D)

...or test it here:

```strudel
s("bd sd").osc()
```

If you now hear sound, congratulations! If not, you can get help on the [#strudel channel in the TidalCycles discord](https://discord.com/invite/HGEdXmRkzT).

Note: if you have the 'Audio Engine Target' in settings set to 'OSC', you do not need to add .osc() to the end of your pattern.

### Pattern.osc

<JsDoc client:idle name="Pattern.osc" h={0} />

## SuperDirt Params

Please refer to [Tidal Docs](https://tidalcycles.org/) for more info.

<br />

But can we use Strudel [offline](/learn/pwa)?

# MQTT

MQTT is a lightweight network protocol, designed for 'internet of things' devices. For use with strudel, you will
need access to an MQTT server known as a 'broker' configured to accept secure 'websocket' connections. You could
run one yourself (e.g. by running [mosquitto](https://mosquitto.org/)), although getting an SSL certificate that
your web browser will trust might be a bit tricky for those without systems administration experience.
Alternatively, you can use [a public broker](https://www.hivemq.com/mqtt/public-mqtt-broker/).

Strudel does not yet support receiving messages over MQTT, only sending them.

## Usage

The following example shows how to send a pattern to an MQTT broker:

```strudel
"hello world"
    .mqtt(undefined, // username (undefined for open/public servers)
          undefined, // password
          '/strudel-pattern', // mqtt 'topic'
          'wss://mqtt.eclipseprojects.io:443/mqtt', // MQTT server address
          'mystrudel', // MQTT client id - randomly generated if not supplied
          0 // latency / delay before sending messages (0 = no delay)
         )
```

Other software can then receive the messages. For example using the [mosquitto](https://mosquitto.org/) commandline client tools:

```

> mosquitto_sub -h mqtt.eclipseprojects.io -p 1883 -t "/strudel-pattern"
> hello
> world
> hello
> world
> ...

```

Control patterns will be encoded as JSON, for example:

```strudel
sound("sax(3,8)").speed("2 3")
  .mqtt(undefined, // username (undefined for open/public servers)
        undefined, // password
        '/strudel-pattern', // mqtt 'topic'
        'wss://mqtt.eclipseprojects.io:443/mqtt', // MQTT server address
        'mystrudel', // MQTT client id - randomly generated if not supplied
        0 // latency / delay before sending messages (0 = no delay)
       )
```

Will send messages like the following:

```

{"s":"sax","speed":2}
{"s":"sax","speed":2}
{"s":"sax","speed":3}
{"s":"sax","speed":2}
...

```

Libraries for receiving MQTT are available for many programming languages.

```

```


---

# Input Devices

Strudel supports various input devices like Gamepads and MIDI controllers to manipulate patterns in real-time.

<Gamepad />


---

# Frequently Asked Questions

This page contains frequently asked questions, with answers. Usually, the topic is explained in more detail in a section which is linked in the answer.

## Is Strudel/Tidal free?

Yes - there is no charge, this is a collective open source project, and the music you make with it is your own. However if you can, please make a one-off or regular donation to our [opencollective fund](https://opencollective.com/tidalcycles), that supports the software and cultural development of Strudel and other Uzu languages.

While there is no charge there are some caveats, e.g.:

- the source code must stay free, i.e. you cannot distribute strudel or tidal as part of projects with incompatible licenses - see the [license](https://www.gnu.org/licenses/agpl-3.0.en.html) for details.
- the contributed examples and tracks are also separately licensed, and must not e.g. be used to train AI models without permission.

## How do I try out the latest features?

The main, stable strudel website is [strudel.cc](https://strudel.cc/). There is also [warm.strudel.cc](https://warm.strudel.cc), known as "warm strudel", which has the latest development features. You might find warm strudel has bug fixes and features that the main website doesn't, but it will often be less stable and probably not suitable for important performances.

Alternatively, you can run strudel locally to try out the latest features. You can find development-oriented [instructions for that here](https://codeberg.org/uzu/strudel/src/branch/main/CONTRIBUTING.md#project-setup).

You can see the [latest changes here](https://codeberg.org/uzu/strudel/pulls?q=&type=all&sort=recentupdate&state=closed&labels=&milestone=0&project=0&assignee=0&poster=0), as 'pull requests'.

## How to record or export audio?

Strudel is not a digital audio workstation and does not operate following the same principles shared by most traditional audio softwares. However, there are multiple ways to record the audio -- and video -- output of Strudel:

- Use the 'export' tab to render and download as an audio file.
- capture the raw stereo signal coming out of your web browser. You will need an external audio editor/DAW such as Reaper/Audacity/Ardour, etc.
- use the alternative SuperDirt audio engine. Read [this page](/learn/input-output/#oscsuperdirtstrudeldirt) to know more about it.
- capture the audio/video stream using a capture tool such as [OBS](https://obsproject.com/fr), which is designed for live streaming, but also works very well for recording.
- don't record anything and code it again in front of your friends.

## Can I use strudel with my IDE?

Yes you can. There are experimental modes, made by community members, for several IDEs such as:

- VS Code: [Strudel VS](https://marketplace.visualstudio.com/items?itemName=cmillsdev.strudelvs): an experimental mode for Microsoft VSCode. A revived version of [TidalStrudel](https://marketplace.visualstudio.com/items?itemName=roipoussiere.tidal-strudel), which is defunct.
- nvim: [strudel.nvim](https://github.com/gruvw/strudel.nvim)

## How can I use my own samples?

There are multiple ways to load your sample collection. Some methods are good for quick experimentation, some others are good to share your audio collection with other musicians:

- Import folders [from the interface](/learn/samples/#from-disk-via-import-sounds-folder). These are stored locally in your web browser, and not uploaded.
- Serve a folder of samples locally using the [strudel 'sampler' commandline tool](https://strudel.cc/learn/samples/#from-disk-via-strudelsampler). This can be most reliable method, but requires [nodejs](https://nodejs.org) to be installed.
- Host your sound library online on the web and [load them from an URL](/learn/samples/#loading-custom-samples)

## Can I use Strudel with AI/LLM tools?

You are free to do what you like with Strudel, within the terms of the free/open source AGPLv3 license.
However as a community we are interested in exploring human creativity. AI is _way_ over-hyped right now,
including by people with very shady motives. Many in the community are very wary of people training models
on their tunes that they've poured their love into. So please keep discussion and questions around AI and
LLMs to channels dedicated to the topic and be fully respectful of other people's work.

Furthermore, tools like ChatGPT generally give wrong answers. Please don't ask the community to fix those
answers for you, as generally they will be timewasting nonsense.

Human questions are always welcome!

## Where can I download loads of patterns to train my LLM?

You cannot, as there is no such place. For details regarding our stance towards AI/LLM, see [above](/learn/faq/#can-i-use-strudel-with-aillm-tools)

## How to run offline?

Strudel works offline just fine! There are multiple techniques for this, see [this explanation](learn/pwa/#using-strudel-offline).

## How to change tempo? How do I translate BPM to cpm?

Strudel works in cycles, rather than beats, but if you assume a certain number of beats per cycle, you can convert between them.

For example, if you have your tempo in beats per minute and use 4 beats per cycle (e.g. if your track is in 4/4ths) then you can do `setcpm(BPM/4)`
where BPM is your beats per minute.

If you have a different number of beats per bar or are using more or less beats per cycle (e.g. If you want to put only half a bar or
two bars into one cycle), adjust accordingly.

## Where can I see all the functions?

If you pop open the sidetab of strudel.cc (small white < on the right hand side), there is a tab "reference" which lists all the functions of strudel.

## Where can I see all the samples and synths?

If you pop open the sidetab of strudel.cc (small white < on the right hand side), there is a tab "sounds" which lists all the drum machines, samples and synths currently loaded.

## How do I use this exactly like a DAW?

Strudel has different design aims for a DAW, and so treating it like one will likely be frustrating. DAWs are geared towards
sequencing notes over time in predictable ways, whereas Strudel and similar Uzu languages are geared towards combining and
transforming patterns in ways that can be hard to predict.

If you want to emulate the functionality of a DAW in Strudel, you'll have to identify the operations
executed by the DAW (sequencing, repeating, applying filters and envelopes) and write code that is equivalent to these
operations. For example in Strudel, the 'arrange' and 'pick' methods are useful for sequencing patterns over time (see question on these later in this document).

You might still find that the typical DAW workflow is not really adapted to live coding because, despite
both being ways of making music on the computer, they are two very different tools. You could then adapt your way of proceeding
to the medium of code, which might mean leaving more place to serendipity and writing code that you don't predict the output of.

## Why doesn't everyone just use a DAW?

There is no easy answer to this question. Here are some thoughts:

- Live coding tools such as Strudel are excellent for improvising music and visuals using a computer. DAWs are valuable and robust companions for other activities such as producing, mastering and mixing audio, among other usages. Using a tool does not exclude from using any another tool, just build a toolbox.

- Live coding has developed over decades as a distinct creative practice. For example, live coding artists like to show their screens while playing in front of an audience. It is an essential part of what they do, of the way they share their activity with everybody.

- Code is a human language, it is made for other humans to read it. You can read the code and enjoy the music too. It has meaning, value, and there might even be something poetic/important about it! - Strudel is free and open source, you can inspect the code, reshape it, contribute to it if you can/want. It is not opaque and this matters for many people. There is no black box, no obscure abstractions, no business model, no user tracking or hidden features. We need open tools in the arts! - Live coders don't all shy away from using DAWs. Many use them all of the time, especially when it makes their life easier for... live coding!

- Code is an artistic material like any other. There is something valuable in the process of making music through code. More generally speaking, it is nice to tackle creative problems through the use of a programming language: creative thinking, building up your own solutions, DIY approach to music-making, unexpected outcome of algorithms, funny human errors, etc.

- There are pianos and trumpets in your DAW: why do people continue playing the piano or the trumpet? Think of live coding tools as instruments that you activate through the act of programming.

## How can I interface Strudel with my favorite music software? What can I do with it?

Strudel can send [MIDI and OSC](/learn/input-output/), which are protocols for communicating musical information.

Other music software (or hardware!) can then listen to these messages and process them according to its capabilities.

A simple example would be to send livecoded audio to a DAW like Ardour on different tracks and then use it to mix them.

You could also send the MIDI of a sequenced pattern to Musescore and then have it transcribe your livecoded work as a musical score.

You could also send MIDI to your hardware synths, if you like their sound.

## How do I use this in my closed source webgame or other software?

You don't. You need to license your game to a free/open source license fulfill the [AGPLv3 license](https://codeberg.org/uzu/strudel/src/branch/main/LICENSE) Strudel is distributed under.

## How to play different patterns simultaneously?

Using the $ operator, several patterns can be played at once:

```strudel
$: s("bd*4").bank("tr707")
$: s("- sd").bank("tr909")
```

See also [stack](intro/#combining-patterns)

## Is it possible to mute a pattern?

With an additional underscore, a pattern can be muted.

```strudel
$: s("bd*4").bank("tr707")
_$: s("- sd").bank("tr909")
```

See also [hush](/learn/conditional-modifiers/#hush)

## How can I arrange in Strudel using `mask`?

With mini-notation, using the `<>` and `!` operators, you can try something like

```
.mask("<0!24 1!40>")
```

It mutes a pattern for 24 cycles and plays it for 40. You would gain 64 cycles total, a multiple of 2/4/8 commonly used in western music.

If each cycle is a bar, as a starting point, you could write a mask like that for any pattern:

```
.mask("<0!16 0!16 0!16 0!16 0!16 0!10>")
```

It mutes it throughout.

For arranging, you could add the same mask to each part and replace some zeroes with ones in your different masks to make parts play.

If you use `.mask()` on different patterns mess up your counting, then patterns do not align anymore.
On the other hand, doing that on purpose is one of the things that could be considered a strength of tidalcycles and Strudel.
You can make things quite lively and more organic with a little (controlled) interference, according to your own taste.
And you are free to arrange in cycles like 3, 6 or 9 too.

To modify everything at once, you could try all and when, for example:

```
all(x=>x.when("<0!7 1>", x=>x.lpf(saw.range(200, 2000))))
```

This would lowpass filter sweep everything every 8 cycles.

## How can I arrange in Strudel using `arrange` or `pick`?

Take [Pachelbel's Canon in D](https://en.wikipedia.org/wiki/Pachelbel%27s_Canon#Analysis) as an example which has 4 voices (one cello and 3 violins) which have repeating patterns, as seen in the link above.

The following snipped defines the patterns as constants which can then be used for the different voices. `arrange` takes multiple arguments, which are each a number of cycles and a pattern which is played for the number of cycles, wrapped in `[]` If the pattern is shorter than the number, it is repeated.

```strudel
const cello = note(
  "<[d3 a2 b2 f#2] [g2 d3 g2 a2]>")
  .color("grey").sound("gm_tremolo_strings:3")
 const violin_p1 = note(
  "<[f#5 e5 d5 c#5] [b4 a4 b4 c#5]>")
  .color("blue")
 const violin_p2 = note(
  "<[d5 c#5 b4 a4] [ g4 f#4 g4 f#4]>")
 .color("green")
 const violin_p3 = note(
  "<[d4 f#4 a4 g4 f#4 d4 f#4 e4] [d4 b3 d4 a4 g4 b4 a4 g4]>")
  .color("purple")
 const violin_p4 = note(
  "<[f#4 d4 e4 c#5 d5 f#5 a5 a4] [b4 g4 a4 f#4 d4 d5 [d5@3 c#5]@2]>")
  .color("red")

cello$: arrange(
  [2, silence],
  [18,cello])
 violin1$: arrange(
[4,silence],
[2,violin_p1], [2,violin_p2],
[2,violin_p3], [2,violin_p4],
[2,violin_p1], [2,violin_p2],
[2,violin_p3], [2,violin_p4]
).sound("gm_tremolo_strings:0")
violin2$: arrange(
  [6,silence], [2,violin_p1], 
  [2,violin_p2], [2,violin_p3], 
  [2,violin_p4], [2,violin_p1], 
  [2,violin_p2], [2,violin_p3] 
  ).sound("gm_tremolo_strings:1")
 violin3$: arrange(
[8,silence],
[2,violin_p1], [2,violin_p2],
[2,violin_p3], [2,violin_p4],
[2,violin_p1], [2,violin_p2]
).sound("gm_tremolo_strings:2")

    all(x => x.release(.2))

```

Alternatively, you can also put the different patterns for the violins into one single array (`const violins = [violin_p1, violin_p2, violin_p3, violin_p4]`) and use a pattern as an index to `pick` the nth element of that array. This replaces the voices defined above. Here you use `0@2` to specifiy that the first item (i.e. with index `0`) is played for `2` cycles.

`pick` has better highlighting than `arrange`:

```strudel
const cello = note(
  "<[d3 a2 b2 f#2] [g2 d3 g2 a2]>")
  .color("grey").sound("gm_tremolo_strings:3")
 const violin_p1 = note(
  "<[f#5 e5 d5 c#5] [b4 a4 b4 c#5]>")
  .color("blue")
 const violin_p2 = note(
  "<[d5 c#5 b4 a4] [ g4 f#4 g4 f#4]>")
 .color("green")
 const violin_p3 = note(
  "<[d4 f#4 a4 g4 f#4 d4 f#4 e4] [d4 b3 d4 a4 g4 b4 a4 g4]>")
  .color("purple")
 const violin_p4 = note(
  "<[f#4 d4 e4 c#5 d5 f#5 a5 a4] [b4 g4 a4 f#4 d4 d5 [d5@3 c#5]@2]>")
  .color("red")

const violins = [violin_p1, violin_p2, violin_p3, violin_p4]

cello$: "<~@2 0@18>".pick([cello])
violin1$: "<~@4 0@2 1@2 2@2 3@2 0@2 1@2 2@2 3@2>".pick(violins)
.sound("gm_tremolo_strings:0")
violin2$: "<~@6 0@2 1@2 2@2 3@2 0@2 1@2 2@2>".pick(violins)
.sound("gm_tremolo_strings:1")
violin3$: "<~@8 0@2 1@2 2@2 3@2 0@2 1@2 >".pick(violins)
.sound("gm_tremolo_strings:2")
all(x => x.release(.2))

```

The `pick` method also works with jsons which have named elements, which makes it easier to read, see the [here](/learn/conditional-modifiers/#pick). `pickRestart` restarts the pattern upon picking it which can make a difference if the duration of the pick indexes doesn't line up with the patterns which are picked - which is not the case here.

Try adding `.punchcard()` after the `release(.2)` for a visualization.

## I saw Switch Angel using functions which I cannot find in the reference (e.g. `trancegate`). How do I make it work?

Methods like `trancegate()`, `rlpf()` and `acidenv()` are currently not pattern methods which come natively with strudel.

They are part of a script/prebake for strudel which was written by Switch Angel and published [here](https://github.com/switchangel/strudel-scripts)

You can find the instructions how to use that script in the readme.md there.

## Is there difference between `n` and `note`?

They are not aliases of each other, in contrast to `s` and `sound`.

The method `note` is used to reference a certain note (either as its name, such as `c` or `b2` or the midi number `69`, for example `note("c3 e3 g3")`).

On the other hand, `n` is a way to reference the nth index of something. This something can be a scale (eg `n("0 2 4").scale("C:major")`) , but it can also be a particular note in a chord (see https://strudel.cc/recipes/recipes/#arpeggios for an example) .

The method `n` can also be used for something completely unrelated to notes, in particular the nth sample from a sample map `s("hh*8").bank("RolandTR909").n("0 1 2 3")`.

```strudel

        n("<[0 1 2 3@3 -@2] [3 2 1 0@3 -@2] >")
        .scale("A:minor:pentatonic")
        .s("gm_acoustic_guitar_steel").n("<0 1 2 3>/2")
```

Note that `n` is not the only way that functions use indices, some take numbered patterns instead.

## Is there a cheat sheet for all symbols?

Yes!

```
'   marks start and end of strings, is different from "
"   marks start and end of single line patterns in mini notation, is different from '
`   marks start and end of patterns with line breaks in mini notation, is different from '
[]  used for patterns in mini notation, each item in it has the same length
<>  used for patterns, alternates between items each cycle
{}  historically used for polyrhythmic patterns. {a b c}%4 is the same as <a b c>*4.
@3  elongates the item by a factor of 3 (other numbers work too, even non-integer, but for numbers between 0 and 1 you need a leading zero like this: @0.5)
@   after an item: elongates the item once (multiple @ work too c @ @ is the same as c@3)
_   after an item: also elongates an item once (multiple _ work too c _ _ is the same as c@3), see below for a different usage.
.   this divides equal parts of a pattern and is called a foot. Can be used instead of [] like this: "1 6 7 8 . 2 . 3 . 4" is the same as "[1 6 7 8] 2 3 4"
-   silence
~   also silence
x   not silence (for the use in struct, any non-silence symbol works there)
b   decrease by one semitone, i.e. flat, works for steps of scales, note names (but not midi numbers) and chord names
s   increase by one semitone, i.e. sharp, works for steps of scales, note names (but not midi numbers) but not chord names
#   increase by one semitone, i.e. sharp works for steps of scales, note names (but not midi numbers) and chord names
#   also used in mondo notation
*3  play the sample or pattern at thrice the speed, fast(3)
!3  play the sample or pattern three times
/2  play the sample or pattern at half speed, slow(2)
?   play the pattern sometimes
|   once per cycle, choose randomly a pattern of those separated by i.e. chooseCycles()
,   play all items separated by it at the same time, i.e. stack()
:   is used to separate multiple parameters, such as adsr(".1:.1:.5:.2"), this is is an operator which creates a list of these objects.
$:  at the start of a line, defines a member of the stack. is the only stack name that should occur multiple names
_   before a stack name: mutes the stack, i.e. hush(), for example _$: s("bd"), see above for a different usage.
```


---

# Using CSound with Strudel

🧪 Strudel has experimental support for csound, using [@csound/browser](https://www.npmjs.com/package/@csound/browser).

## Importing .orc files

To use existing csound instruments, you can load and use an orc file from an URL like this:

```strudel
// livecode.orc by Steven Yi
await loadOrc('github:kunstmusik/csound-live-code/master/livecode.orc')
note("c a f e").csound('FM1')

```

Note that the above url uses the `github:` shortcut, which resolves to the raw file on github, but you can use any URL you like.

The awesome [`livecode.orc by Steven Yi`](https://github.com/kunstmusik/csound-live-code) comes packed with many sounds ready for use:

```strudel
// livecode.orc by Steven Yi
await loadOrc('github:kunstmusik/csound-live-code/master/livecode.orc')
note("c a f e").csound(cat(
"Sub1", // 	Substractive Synth, 3osc
"Sub2", // 	Subtractive Synth, two saws, fifth freq apart
"Sub3", // 	Subtractive Synth, three detuned saws, swells in
"Sub4", // 	Subtractive Synth, detuned square/saw, stabby. Nice as a lead in octave 2, nicely grungy in octave -2, -1
"Sub5", // 	Subtractive Synth, detuned square/triangle
"Sub6", // 	Subtractive Synth, saw, K35 filters
"Sub7", // 	Subtractive Synth, saw + tri, K35 filters
"Sub8", // 	Subtractive Synth, square + saw + tri, diode ladder filter
"SynBrass", // 	SynthBrass subtractive synth
"SynHarp", // 	Synth Harp subtracitve Synth
"SSaw", // 	SuperSaw sound using 9 bandlimited saws (3 sets of detuned saws at octaves)
"Mode1", // 	Modal Synthesis Instrument: Percussive/organ-y sound
"Plk", // 	Pluck sound using impulses, noise, and waveguides
"Organ1", // 	Wavetable Organ sound using additive synthesis
"Organ2", // 	Organ sound based on M1 Organ 2 patch
"Organ3", // 	Wavetable Organ using Flute 8' and Flute 4', wavetable based on Claribel Flute http://www.pykett.org.uk/the\_tonal\_structure\_of\_organ\_flutes.htm
"Bass", // 	Subtractive Bass sound
"ms20_bass", // 	MS20-style Bass Sound
"VoxHumana", // 	VoxHumana Patch
"FM1", // 	FM 3:1 C:M ratio, 2->0.025 index, nice for bass
"Noi", // 	Filtered noise, exponential envelope
"Wobble", // 	Wobble patched based on Jacob Joaquin's "Tempo-Synced Wobble Bass"
"Sine", // 	Simple Sine-wave instrument with exponential envelope
"Square", // 	Simple Square-wave instrument with exponential envelope
"Saw", // 	Simple Sawtooth-wave instrument with exponential envelope
"Squine1", // 	Squinewave Synth, 2 osc
"Form1", // 	Formant Synth, buzz source, soprano ah formants
"Mono", // 	Monophone synth using sawtooth wave and 4pole lpf. Use "start("Mono") to run the monosynth, then use MonoNote instrument to play the instrument.
"MonoNote", // 	Note playing instrument for Mono synth. Be careful to use this and not try to create multiple Mono instruments!
"Click", // 	Bandpass-filtered impulse glitchy click sound. p4 = center frequency (e.g., 3000, 6000)
"NoiSaw", // 	Highpass-filtered noise+saw sound. Use NoiSaw.cut channel to adjust cutoff.
"Clap", // 	Modified clap instrument by Istvan Varga (clap1.orc)
"BD", // 	Bass Drum - From Iain McCurdy's TR-808.csd
"SD", // 	Snare Drum - From Iain McCurdy's TR-808.csd
"OHH", // 	Open High Hat - From Iain McCurdy's TR-808.csd
"CHH", // 	Closed High Hat - From Iain McCurdy's TR-808.csd
"HiTom", // 	High Tom - From Iain McCurdy's TR-808.csd
"MidTom", // 	Mid Tom - From Iain McCurdy's TR-808.csd
"LowTom", // 	Low Tom - From Iain McCurdy's TR-808.csd
"Cymbal", // 	Cymbal - From Iain McCurdy's TR-808.csd
"Rimshot", // 	Rimshot - From Iain McCurdy's TR-808.csd
"Claves", // 	Claves - From Iain McCurdy's TR-808.csd
"Cowbell", // 	Cowbell - From Iain McCurdy's TR-808.csd
"Maraca", // 	Maraca - from Iain McCurdy's TR-808.csd
"HiConga", // 	High Conga - From Iain McCurdy's TR-808.csd
"MidConga", // 	Mid Conga - From Iain McCurdy's TR-808.csd
"LowConga", // 	Low Conga - From Iain McCurdy's TR-808.csd
))
```

## Writing your own instruments

You can define your own instrument(s) with `loadCsound` like this:

```strudel
await loadCsound\`
instr CoolSynth
    iduration = p3
    ifreq = p4
    igain = p5
    ioct = octcps(ifreq)

    kpwm = oscili(.05, 8)
    asig = vco2(igain, ifreq, 4, .5 + kpwm)
    asig += vco2(igain, ifreq * 2)

    idepth = 2
    acut = transegr:a(0, .005, 0, idepth, .06, -4.2, 0.001, .01, -4.2, 0) ; filter envelope
    asig = zdf_2pole(asig, cpsoct(ioct + acut + 2), 0.5)

    iattack = .01
    isustain = .5
    idecay = .1
    irelease = .1
    asig *= linsegr:a(0, iattack, 1, idecay, isustain, iduration, isustain, irelease, 0)

    out(asig, asig)

endin\`

"<0 2 [4 6](3,4,2) 3\*2>"
.off(1/4, add(2))
.off(1/2, add(6))
.scale('D minor')
.note()
.csound('CoolSynth')
```

## Parameters

The `.csound` function sends the following p values:

|     |                                  |
| --- | -------------------------------- |
| p1  | instrument name e.g. `CoolSynth` |
| p2  | time offset, when it should play |
| p3  | the duration of the event / hap  |
| p4  | frequency in Hertz               |
| p5  | normalized `gain`, 0-1           |

There is an alternative `.csoundm` function with a different flavor:

|     |                                   |
| --- | --------------------------------- |
| p4  | midi key number, unrounded, 0-127 |
| p5  | midi velocity, 0-127              |

In both cases, p4 is derived from the value of `freq` or `note`.

## Limitations / Future Plans

Apart from the above listed p values, no other parameter can be patterned so far.
This also means that [audio effects](/learn/effects/) will not work.
In the future, the integration could be improved by passing all patterned control parameters to the csound instrument.
This could work by a unique [channel](https://kunstmusik.github.io/icsc2022-csound-web/tutorial2-interacting-with-csound/#step-4---writing-continuous-data-channels)
for each value. Channels could be read [like this](https://github.com/csound/csound/blob/master/Android/CsoundForAndroid/CsoundAndroidExamples/src/main/res/raw/multitouch_xy.csd).
Also, it might make sense to have a standard library of csound instruments for strudel's effects.

Now, let's dive into the [Functional JavaScript API](/functions/intro)


---

# Using Hydra inside Strudel

You can write [hydra](https://hydra.ojack.xyz/) code in strudel! All you have to do is to call `await initHydra()` at the top:

```strudel
await initHydra()
// licensed with CC BY-NC-SA 4.0 https://creativecommons.org/licenses/by-nc-sa/4.0/
// by Zach Krall
// http://zachkrall.online/

osc(10, 0.9, 300)
.color(0.9, 0.7, 0.8)
.diff(
osc(45, 0.3, 100)
.color(0.9, 0.9, 0.9)
.rotate(0.18)
.pixelate(12)
.kaleid()
)
.scrollX(10)
.colorama()
.luma()
.repeatX(4)
.repeatY(4)
.modulate(
osc(1, -0.9, 300)
)
.scale(2)
.out()

note("[a,c,e,<a4 ab4 g4 gb4>,b4]/2")
.s("sawtooth").vib(2)
.lpf(600).lpa(2).lpenv(6)

```

## H patterns

There is a special function `H` that allows you to use a pattern as an input to hydra:

```strudel
await initHydra()
let pattern = "3 4 5 [6 7]*2"
shape(H(pattern)).out(o0)
n(pattern).scale("A:minor").piano().room(1)

```

## detectAudio

To use hydra audio capture, call `initHydra` with `{detectAudio:true}` configuration param:

```strudel
await initHydra({detectAudio:true})
let pattern = "<3 4 5 [6 7]*2>"
shape(H(pattern)).repeat()
  .scrollY(
    ()=> a.fft[0]*.25
  )
  .add(src(o0).color(.71 ).scrollX(.005),.95)
.out(o0)
n(pattern).scale("A:minor").piano().room(1)

```

You might now be able to see this properly here: [open in REPL](/#YXdhaXQgaW5pdEh5ZHJhKCkKbGV0IHBhdHRlcm4gPSAiMyA0IDUgWzYgN10qMiIKc2hhcGUoSChwYXR0ZXJuKSkub3V0KG8wKQpuKHBhdHRlcm4pLnNjYWxlKCJBOm1pbm9yIikucGlhbm8oKS5yb29tKDEpIA%3D%3D)

Similar to `detectAudio`, all the [available hydra options](https://github.com/hydra-synth/hydra-synth#api) can be passed to `initHydra`.

## feedStrudel

Using the `feedStrudel` option, you can transform strudel visualizations with hydra:

```strudel
await initHydra({feedStrudel:1})
//
src(s0).kaleid(H("<4 5 6>"))
  .diff(osc(1,0.5,5))
  .modulateScale(osc(2,-0.25,1))
  .out()
//

$: s("bd*4,[hh:0:<.5 1>]*8,~ rim").bank("RolandTR909").speed(.9)

$: note("[<g1!3 <bb1 <f1 d1>>>]\*3").s("sawtooth")

.room(.75).sometimes(add(note(12))).clip(.3)
.lpa(.05).lpenv(-4).lpf(2000).lpq(8).ftype('24db')

all(x=>x.fft(4).scope({pos:0,smear:.95}))
```


---

# Accumulation Modifiers

## superimpose

<JsDoc client:idle name="Pattern.superimpose" h={0} />

## layer

<JsDoc client:idle name="Pattern.layer" h={0} />

## off

<JsDoc client:idle name="Pattern.off" h={0} />

## echo

<JsDoc client:idle name="Pattern.echo" h={0} />

## echoWith

<JsDoc client:idle name="echoWith" h={0} />

## stut

<JsDoc client:idle name="stut" h={0} />

There are also [Tonal Functions](/learn/tonal).


---

# Welcome

Welcome to the Strudel documentation pages!

These pages will introduce you to [Strudel](https://strudel.cc/), a web-based [live coding](https://github.com/toplap/awesome-livecoding/) environment that implements the [Tidal Cycles](https://tidalcycles.org) algorithmic pattern language.

# What is Strudel?

[Strudel](https://strudel.cc/) is a version of [Tidal Cycles](https://tidalcycles.org) written in [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), initiated by [Alex McLean](https://slab.org) and [Felix Roos](https://froos.cc/) in 2022.
Tidal Cycles, also known as Tidal, is a language for [algorithmic pattern](https://algorithmicpattern.org), and though it is most commonly used for [making music](https://tidalcycles.org/docs/showcase), it can be used for any kind of pattern making activity, including [weaving](https://www.youtube.com/watch?v=TfEmEsusXjU).

Tidal was first implemented as a library written in the [Haskell](https://www.haskell.org/) functional programming language, and by itself it does not make any sound.
To make sound, it has to be connected to a sound engine, and by default this is a [SuperCollider](https://supercollider.github.io/) plugin called [SuperDirt](https://github.com/musikinformatik/SuperDirt/).
As such, it can be difficult for first-time users to install both Tidal Cycles and SuperDirt, as there are many small details to get right.
Strudel however runs directly in your web browser, does not require any custom software installation, and can make sound all by itself.

# Strudel REPL and MiniREPL

The main place to actually make music with Strudel is the [Strudel REPL](https://strudel.cc/) ([what is a REPL?](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)), but in these pages you will also encounter interactive "MiniREPLs" where you can listen to and edit Strudel patterns.
Try clicking the play icon below:

```strudel
s("bd sd")
```

Then edit the text so it reads `s("bd sd cp hh")` and click the refresh icon.
Congratulations, you have now live coded your first Strudel pattern!

With Strudel, you can expressively write dynamic music pieces.
You don't need to know JavaScript or Tidal Cycles to make music with Strudel.
This interactive tutorial will guide you through the basics of Strudel.

# Show me some demos!

To see and hear what Strudel can do, visit the [Strudel REPL](https://strudel.cc/) and click the Shuffle icon in the top menu bar.
You can get a feel for Strudel by browsing and editing these examples and clicking the Refresh icon to update.

You can also browse through the examples [here](/examples).

Alternatively, you can get a taste of what Strudel can do by clicking play on this track:

```strudel
samples({
  bd: ['bd/BT0AADA.wav','bd/BT0AAD0.wav','bd/BT0A0DA.wav','bd/BT0A0D3.wav','bd/BT0A0D0.wav','bd/BT0A0A7.wav'],
  sd: ['sd/rytm-01-classic.wav','sd/rytm-00-hard.wav'],
  hh: ['hh27/000_hh27closedhh.wav','hh/000_hh3closedhh.wav'],
}, 'github:tidalcycles/dirt-samples');
stack(
s("bd,[~ <sd!3 sd(3,4,2)>],hh*8") // drums
.speed(perlin.range(.7,.9)) // random sample speed variation
,"<a1 b1\*2 a1(3,8) e2>" // bassline
.off(1/8,x=>x.add(12).degradeBy(.5)) // random octave jumps
.add(perlin.range(0,.5)) // random pitch variation
.superimpose(add(.05)) // add second, slightly detuned voice
.note() // wrap in "note"
.decay(.15).sustain(0) // make each note of equal length
.s('sawtooth') // waveform
.gain(.4) // turn down
.cutoff(sine.slow(7).range(300,5000)) // automate cutoff
,"<Am7!3 <Em7 E7b13 Em7 Ebm7b5>>".voicings('lefthand') // chords
.superimpose(x=>x.add(.04)) // add second, slightly detuned voice
.add(perlin.range(0,.5)) // random pitch variation
.note() // wrap in "note"
.s('sawtooth') // waveform
.gain(.16) // turn down
.cutoff(500) // fixed cutoff
.attack(1) // slowly fade in
)
.slow(3/2)
```

# Strudel is a work in progress 🚧

Please note that this project is still in its experimental state.
In the future, parts of it might change significantly.
This tutorial is also far from complete.
You can contribute to it clicking 'Edit this page' in the top right, or by visiting the [Strudel GitHub page](https://codeberg.org/uzu/strudel/).

# What's next?

Head on over to the [Notes](/learn/notes) page.

<br />


---

# Comparing Strudel and Tidal

This page is dedicated to exisiting tidal users, giving an overview of all the differences between Strudel and Tidal.

## Language

Strudel is written in JavaScript, while Tidal is written in Haskell.

### Example

This difference is most obvious when looking at the syntax:

```haskell
iter 4 $ every 3 (||+ n "10 20") $ (n "0 1 3") # s "triangle" # crush 4
```

One _could_ express that pattern to Strudel like so:

```
iter(4, every(3, add.squeeze("10 20"), n("0 1 3").s("triangle").crush(4)))
```

- The `$` operator does not exist, so the `iter` function has to wrap everything in parens.
- Custom operators like `||+` are explicit function calls, `add.squeeze` in this case
- The `#` operator is replaced with a chained function call `# crush 4` => `.crush(4)`

Unlike Haskell, JavaScript lacks the ability to define custom infix
operators, or change the meaning of existing ones.

Before you discard Strudel as an unwieldy paren monster, look at this alternative way to write the above:

```
n("0 1 3").every(3, add.squeeze("10 20")).iter(4).s("triangle").crush(4)
```

By reordering calls, the parens are much less nested.
As a general rule by thumb, you could say that everything Tidal does with `$` is reversed in Strudel:

`iter 4 $ every 3 (||+ n "10 20") $ (n "0 1 3")`

becomes

`n("0 1 3").every(3, add.squeeze("10 20")).iter(4)`

Simply put, `foo x $ bar x` becomes `bar(x).foo(x)`.

### Operators

The [custom operators of tidal](https://tidalcycles.org/docs/reference/pattern_structure/#all-the-operators) are normal functions in strudel:

| function    | tidal  | strudel |
| ----------- | ------ | ------- |
| add         | \|+ n  | .add(n) |
| subtract    | \|- n  | .sub(n) |
| multiply    | \|\* n | .mul(n) |
| divide      | \|\/ n | .div(n) |
| modulo      | \|\% n | .mod(n) |
| left values | \|\< n | .set(n) |

The above list only displays the operators taking the structure comes from the `left`.
For each of those, a `right` and `both` variant also exists.
As this directional thinking only works with code, strudel calls these `in` / `out` / `mix`:

| direction | tidal   | strudel     |
| --------- | ------- | ----------- |
| left      | \|+ n   | .add.in(n)  |
| right     | +\| n   | .add.out(n) |
| both      | \|+\| n | .add.mix(n) |

Instead of `+` / `add`, you can use any of the available operators of the first list.

## Function Compatibility

[This issue](https://codeberg.org/uzu/strudel/issues/31) tracks which Tidal functions are implemented in Strudel.
The list might not be 100% up to date and probably also misses some functions completely..
Feel encouraged to search the source code for a function you're looking for.
If you find a function that's not on the list, please tell!

## Control Params

As seen in the example, the `#` operator (shorthand for `|>`) is also just a function call in strudel.
So `note "c5" # s "gtr"` becomes `note("c5").s('gtr')`.

[This file](https://codeberg.org/uzu/strudel/src/branch/main/packages/core/controls.mjs) lists all available control params.
Note that not all of those work in the Webaudio Output of Strudel.
If you find a tidal control that's not on the list, please tell!

## Sound

Tidal is commonly paired with Superdirt / Supercollider for sound generation.
While Strudel also has a way of [communicating with Superdirt](/learn/input-output/),
it aims to provide a standalone live coding environment that runs entirely in the browser.

### Audio Effects

Many of SuperDirt's effects have been reimplemented in Strudel, using the Web Audio API.
You can find a [list of available effects here](/learn/effects/).

### Sampler

Strudel's sampler supports [a subset](/learn/samples) of Superdirt's sampler.
Also, samples are always loaded from a URL rather than from the disk, although [that might be possible in the future](https://codeberg.org/uzu/strudel/issues/118).

## Evaluation

The Strudel REPL does not support [block based evaluation](https://codeberg.org/uzu/strudel/issues/34) yet.
You can use labeled statements and `_` to mute:

`$: n("[0 .. 8]*8/9").scale("C:minor:pentatonic")

\_$: s("bd\*4").bank('RolandTR909')`

## Tempo

Strudels tempo is 1 cycle per second, while tidal defaults to `0.5625`.
You can get the same tempo as tidal with:

```
note("c a f e").fast(.5625);
```

Next up: the [REPL](/technical-manual/repl)


---

# Mondo Notation

"Mondo Notation" is a new kind of notation that is similar to [Mini Notation](/learn/mini-notation/), but with enough abilities to make it work as a standalone pattern language.
Here's an example:

```strudel
$ note (c2 # euclid <3 6 3> <8 16>) # *2 
  # s "sine" # add (note [0 <12 24>]*2)
  # dec(sine # range .2 2) 
  # room .5
  # lpf (sine/3 # range 120 400)
  # lpenv (rand # range .5 4)
  # lpq (perlin # range 5 12 # * 2)
  # dist 1 # fm 4 # fmh 5.01 # fmdecay <.1 .2>
  # postgain .6 # delay .1 # clip 5

$ s [bd bd bd bd] # bank tr909 # clip .5

# ply <1 [1 [2 4]]>

$ s oh\*4 # press # bank tr909 # speed.8

# dec (<.02 .05>\*2 # add (saw/8 # range 0 1))

```

## Mondo in the REPL

For now, you can only use mondo in the repl like this:

```strudel
mondo`s hh*8`
```

The rest of this site will only use the mondo notation itself.
In the future, the REPL might get a way to use mondo notation directly.

## Calling Functions

Compared to Mini Notation, the most notable feature of Mondo Notation is the ability to call functions using round brackets:

```strudel
(s hh*8)
```

The first element inside the brackets is the function name. In JS, this would look like:

```strudel
s("hh*8")
```

The outermost parens are not needed, so we can drop them:

```strudel
s hh*8
```

## Mini Notation Features

Besides function calling with round parens, Mondo Notation has a lot in common with Mini Notation:

### Brackets

- `[]` for 1-cycle sequences
- `<>` for multi-cycle sequences
- `{}` for stepped sequences (more on that later)

### Infix Operators

- \* => [fast](/learn/time-modifiers/#fast)
- / => [slow](/learn/time-modifiers/#slow)
- ! => [extend](/learn/stepwise/#extend)
- @ => [expand](/learn/stepwise/#expand)
- % => [pace](/learn/stepwise/#pace)
- ? => [degradeBy](/learn/random-modifiers/#degradeby) (currently requires right operand)
- : => tail (creates a list)
- .. => range (between numbers)
- , => [stack](/learn/factories/#stack)
- | => [chooseIn](/learn/random-modifiers/#choose)

### Example

`note <
[e5 [b4 c5] d5 [c5 b4]]
[a4 [a4 c5] e5 [d5 c5]]
[b4 [~ c5] d5 e5]
[c5 a4 a4 ~]
[[~ d5] [~ f5] a5 [g5 f5]]
[e5 [~ c5] e5 [d5 c5]]
[b4 [b4 c5] d5 e5]
[c5 a4 a4 ~]
>`

## Chaining Functions

Similar to how "." works in javascript (JS), we can chain functions calls with the "#" operator:

```strudel
n <0 2 4 [3 1] -1>*4 
 # scale C4:minor 
 # jux rev 
 # dec .2
 # delay .5
```

Here's the same written in JS:

```strudel
n("<0 2 4 [3 1] -1>*4")
 .scale("C4:minor")
 .jux(rev)
 .dec(.2)
 .delay(.5)
```

### Chaining Functions Locally

A function can be applied to a single element by wrapping it in round parens:

```strudel
s [bd hh bd (cp # delay .6)] # bank tr909
```

in this case, `delay .6` will only be applied to `cp`. compare this with the JS version:

```strudel
s(seq("bd", "hh", "bd", "cp".delay(.6))).bank('tr909')
```

here we can see how much we can save when there's no boundary between mini notation and function calls!

### Chaining Infix Operators

Infix operators exist as regular functions, so they can be chained as well:

```strudel
s [bd hh] # bank tr909 # *2
```

In this case, the \*2 will be applied to the whole pattern.

### Lambda Functions

Some functions in strudel expect a function as input, for example:

```strudel
n("0 .. 7").scale("C:minor").sometimes(x=>x.dec(.1))
```

in mondo, the `x=>x.` can be shortened to:

```strudel
n 0..7 # scale C:minor # sometimes (# dec .1)
```

chaining works as expected:

```strudel
n 0..7 # scale C:minor # sometimes (# dec .1 # jux rev)
```

## Strings

You can use "double quotes" and 'single quotes' to get a string:

```strudel
n 0..7 # scale 'C minor'
```

## Multiple Patterns

The `$` sign can be used to separate multiple patterns:

```strudel
$ s [bd rim [~ bd] rim] # bank tr707
$ chord <Dm9!3 Db7> # voicing
  # struct[x ~ ~ x ~ x ~ ~] # delay .5
```

The `$` sign is an alias for `,` so it will create a stack behind the scenes.

## variables

using the `def` keyword, you can define variables:

```strudel

$ def melody [0 1 2 3]
$ n melody # scale C:minor

```


---

# Xenharmonic Functions (experimental)

{/* TODO expand explanation of xenharmony */}

These functions allow the use of scales other than your typical chromatic 12 based ones.

### tune(scale)

{/* TODO (maybe): combine jsdoc things in tune.mjs with here */}

<JsDoc client:idle name="tune" h={0} />

Here's an example of how to configure a basic hexany scale:

```strudel
i("0 1 2 3 4 5").tune("hexany15").mul("220").freq()
```

Try other scales like `hexany1`, `iraq`, `gumbeng`, `gunkali`, or `tranh3`

For a full list of available scales from tunejs, see http://abbernie.github.io/tune/scales.html

You can set your root to be a particular note with `getFreq`

```strudel
i("4 8 9 10 - - 5 7 9 11 - -").tune("tranh3")
    .mul(getFreq('c3'))
    .freq().clip(.5).room(1)
```

Some tunings become more pronounced with a longer reverb decay:

```strudel
i("<[5 6 8 10] - [5 7 9 12] -> -").tune("gumbeng")
  .mul(getFreq('c3'))
  .freq().clip(.8).room("3:10").rdim(10000).rfade(5)
```

Additionally, you can combo this with `fmap` so that the base note changes:

```strudel
i("9 11 12 10 - - -").tune("gunkali")
  .mul("<c3 c3 a3 d#3>".fmap(getFreq))
  .freq().legato("2 .7").room("1:15").rdim(8500).rlp(14000).rfade(8)
```

Combining this with various polyrhythm tricks can become very evocative:

```strudel
i("<[0 3 1 -] [-1 4 2 8]> ~ ~,<-4 -5>".add(4))
  .tune("iraq")
  .mul("<c3 d3 c#3>".fmap(getFreq))
  .freq().clip(.5).room(1).rfade(9)
```

Another helpful trick when exploring new tunings is to strum them.
Many have a much more enchanting sound that was chosen over many generations of musicians for being strummed.

Take the `sanza` tuning:

```strudel
i("4 5 6 7 8 9").tune("sanza")
  .mul(getFreq('c3'))
  .freq()
```

Notes 7 and 9 will clash quite a bit if you arp them normally. Many tunings will have this sort of sound, and it can feel distracting on its own.
See how close they are on the pitch wheel?

```strudel
i("[7 9]!3").tune("sanza").mul(getFreq('c3')).freq()._pitchwheel()
```

This quality is often due to how the tunings were formed with instruments that were played differently than a piano.
As such, some tunings are much better strummed, with the subtle clash of the detuned notes actually making the sound much more magical:

```strudel
i("[0 1 2 3 4 5 6]@0.3 -"
  .add("<2 5 8 1>"))
  .tune("sanza")
  .mul(getFreq('c3')).freq()
  .legato("3").room(1).rfade(5)
```

Note the legato and reverb effects make sure the sound of the strumming gets to wash together. Alternating the direction of the strum can make the
tones sound even more alive, too.

The `tranh3` tuning has a similar set of notes, with two clashing. You might trying plugging that in above and see if you find a favorite strumming pattern.

You can also give tune a list of frequencies to use as the scale:

```strudel
i("0 1 2 3 4").tune([
    261.6255653006, 
    302.72962012827, 
    350.29154279212, 
    405.32593044476, 
    469.00678383895, 
    523.2511306012
  ]).mul(220).freq();
```

### xen(scaleOrRatios)

{/* TODO add explanation of EDO to documentation */}

<JsDoc client:idle name="Pattern.xen" h={0} />


---

# Using Strudel Offline

You can use Strudel even without a network! When you first visit the [Strudel REPL](https://strudel.cc/),
your browser will download the whole web app including documentation.
When the download is finished (&lt;1MB), you can visit the website even when offline,
getting the downloaded website instead of the online one.

When the site gets updated, your browser will download that update on the next online visit.
When an update is available, the site will refresh after the download is finished.

This works because Strudel is implemented as progessive web app (using [Vite PWA](https://vite-pwa-org.netlify.app/)).

## Samples

While the browser will download the app itself, samples are only downloaded when you're actively using them.
So to make sure a specific set of samples is available when offline, just use them.
Also, only samples from these domains will be cached for offline use:

- `https://raw.githubusercontent.com/*` for samples uploaded to github
- `https://freesound.org/*` / `https://cdn.freesound.org/*` for freesound
- `https://shabda.ndre.gr/.*` for shabda

## Inspecting / Clearing Cache

You can view all cached files in your browser.

### Firefox

- Open the Developer Tools (`Tools > Web Developer > Web Developer Tools`)
- go to `Storage` tab and expand `Cache Storage > https://strudel.cc`.
- or go to the `Application` tab and view the latest updates in `Service Workers`

### Chromium based Browsers

- Open Developer Tools (`Right Click > Inspect`)
- go to the `Application` tab
- view downloaded files under `Cache > Cache Storage`
- view the latest updates in `Service Workers`

## Strudel Standalone App

You can also install Strudel as a standalone app on most devices.
A standalone app has its own desktop / homescreen icon and launches in a separate window,
without the browser ui.

<figure>
  ![Strudel on MacOS](/pwa/strudel-macos.png)
  <figcaption>Strudel on MacOS</figcaption>
</figure>

### Desktop

With a chromium based browser:

1. go to the [Strudel REPL](https://strudel.cc).
2. on the right of the adress bar, click `install Strudel REPL`
3. the REPL should now run as a standalone chromium app

Without a chromium based browser, you can use [nativefier](https://github.com/nativefier/nativefier) to generate a desktop app:

1. make sure you have NodeJS installed
2. run `npx nativefier strudel.cc`

<figure>
  ![Strudel on Linux](/pwa/strudel-linux.png)
  <figcaption>Strudel on Linux</figcaption>
</figure>

### iOS

1. open to the [Strudel REPL](https://strudel.cc/) in safari
2. press the share icon and tab `Add to homescreen`
3. You should now have a strudel app icon that opens the repl in full screen

### Android

1. open to the [Strudel REPL](https://strudel.cc/)
2. Tab the install button at the bottom

Ok, what are [Patterns](/technical-manual/patterns) all about?


---

# Music metadata

You can optionally add some music metadata in your Strudel code, by using tags in code comments:

```js
// @title My Cool Song
// @by John Doe
// @license CC-BY-SA-4.0
```

Like other comments, those are ignored by Strudel, but it can be used by other tools to retrieve some information about the music.

## Alternative syntax

You can also use comment blocks:

```js
/*
@title My Cool Song
@by John Doe
@license CC-BY-SA-4.0
*/
```

Or define multiple tags in one line:

```js
// @title My Cool Song @by John Doe @license CC-BY-SA-4.0
```

The `title` tag has an alternative syntax using quotes (must be defined at the very begining):

```js
// "My Cool Song" @by John Doe
```

## Tags list

Available tags are:

- `@title`: music title
- `@by`: music author(s), separated by comma, eventually followed with a link in `<>` (ex: `@by John Doe <https://example.com>`)
- `@license`: music license(s), separated by comma. Each license should be specified by using the correct identifier in the [https://spdx.org/licenses/](SPDX License List). Example: CC-BY-SA-4.0. Unsure? [Choose a Creative Commons license here](https://creativecommons.org/choose/).
- `@details`: some additional information about the music
- `@url`: web page(s) related to the music (git repository, Soundcloud link, etc.)
- `@genre`: music genre(s) (pop, jazz, etc.)
- `@album`: music album name
- `@tag`: custom tag

Note to tool authors: _Never_ trust that a song has filled those fields with syntactically correct values; make sure your software is robust enough it doesn't break if it encounters bad values

## Multiple values

Some of them accepts several values, using the comma or new line separator, or duplicating the tag:

```js
/*
@by John Doe
    Jane Doe
@genre pop, jazz
@url https://example.com
@url https://example.org
*/
```

You can also add optional prefixes and use tags where you want:

```js
/*
song @by John Doe
samples @by Jane Doe
*/
...
note("a3 c#4 e4 a4") // @by Sandy Sue
```

## Multiline

If a tag doesn't accept a list, it can take multi-line values:

```js
/*
@details I wrote this song in February 19th, 2023.
         It was around midnight and I was lying on
         the sofa in the living room.
*/
```

# Searching meta-data in the online repl

Meta-data can be used in the search field of the patterns tab in the online repl.

For example to search for all patterns by a specific author use the search term

```
by: Ada L
```

or search for patterns with a specific genre like

```
genre: unicorns
```

Hint: If no meta-data property is provided in the search all patterns with a `@title`, `@by` or `@tag` matching the search term will be shown.


---

<DeviceMotion />
