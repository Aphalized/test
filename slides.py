from manim import *
from manim_slides import Slide
greek = TexTemplate(tex_compiler="xelatex", output_format=".xdv")
greek.add_to_preamble(r"""
\usepackage{fontspec}
\setmainfont{Times New Roman}
\usepackage{polyglossia}
\setdefaultlanguage{greek}
""")

class Introduction(Slide):
    def construct(self):
        Title = Text("Τριγωνομετρική απόδειξη του", line_spacing=1, font="Times New Roman", font_size=40).shift(UP*1)
        self.play(FadeIn(Title))
        Title2 = Text("Πυθαγορείου Θεωρήματος", line_spacing=1, font="Times New Roman", font_size=60)
        Title2.set_color_by_gradient(BLUE, LIGHT_PINK, RED)
        self.next_slide()
        self.play(Write(Title2), run_time=3)

class WithTeX(Slide):
    def construct(self):
        im = MathTex(r"i^i = e^{-\frac{\pi}{2}}").scale(2)
        im.set_color_by_gradient(BLUE, LIGHT_PINK, RED)
        giati = Text("Γιατί όμως;", line_spacing=1, font="Times New Roman", font_size=35).shift(UP * 1)
        self.play(Write(im), run_time=3)
        self.next_slide()
        self.play(Write(giati))
        self.next_slide()
        self.play(im.animate.shift(UP * 6.5), FadeOut(giati))
        self.next_slide()


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
