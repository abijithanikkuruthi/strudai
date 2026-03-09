from backend.prompts import render


class TestPromptRendering:
    def test_system_prompt_renders(self):
        result = render("system.j2")
        assert "Hans Strudel" in result

    def test_system_prompt_no_emojis_rule(self):
        result = render("system.j2")
        assert "Do not use emojis" in result

    def test_system_prompt_plain_text_rule(self):
        result = render("system.j2")
        assert "Do not use bold" in result
