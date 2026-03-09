from backend.prompts import render


class TestPromptRendering:
    def test_system_prompt_renders(self):
        result = render("system.j2", workshop_content="")
        assert "StrudelGPT" in result

    def test_system_prompt_includes_workshop_content(self):
        workshop = "## Mini Notation\n\nSequences use spaces."
        result = render("system.j2", workshop_content=workshop)
        assert "## Mini Notation" in result
        assert "Sequences use spaces." in result
        assert "Strudel Reference" in result
