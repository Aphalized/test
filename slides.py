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
        welcome = Text("This is the Manim Slides starter")
        square = Square(color=BLUE)
        dot = Dot(color=RED).shift(RIGHT + UP)

        self.play(FadeIn(welcome))
        self.next_slide()

        self.wipe(welcome, square)
        self.play(FadeIn(dot))

        self.next_slide(loop=True)
        self.play(
            MoveAlongPath(dot, square, rate_func=linear), run_time=2
        )

class WithTeX(Slide):
    def construct(self):
        Title = Text("Τριγωνομετρική απόδειξη του", line_spacing=1, font="Times New Roman", font_size=40).shift(UP*1)
        self.play(FadeIn(Title))
        Title2 = Text("Πυθαγορείου Θεωρήματος", line_spacing=1, font="Times New Roman", font_size=60)
        Title2.set_color_by_gradient(BLUE, LIGHT_PINK, RED)
        self.next_slide()
        self.play(Write(Title2), run_time=3)


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
