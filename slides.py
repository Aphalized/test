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
        self.next_slide()

class WithTeX(Slide):
    def construct(self):
        # Define the vertices of the triangle
        B = DOWN * 3 + LEFT * 5  # Bottom-left corner
        C = DOWN * 3 + RIGHT * 5  # Bottom-right corner
        A = UP * 3 + LEFT * 5  # Top-left corner
        # Create the triangle
        triangle = Polygon(A, B, C, color=WHITE)
        # Label the vertices
        label_A = Text("Α").next_to(A, UL, buff=0.2)
        label_B = Text("Β").next_to(B, DL, buff=0.2)
        label_C = Text("Γ").next_to(C, DR, buff=0.2)
        # Add the triangle to the scene
        self.play(Create(triangle))
        # Add the 90-degree angle label
        right_angle_marker = RightAngle(Line(B, C), Line(B, A), length=0.4, color=YELLOW)

        self.play(Create(right_angle_marker))

        # Add vertex labels to the scene
        self.play(Write(label_A), run_time=0.5)
        self.play(Write(label_B), run_time=0.5)
        self.play(Write(label_C), run_time=0.5)
        self.next_slide()
        # Label the sides
        label_a = Text("α").next_to(Line(A, B).get_midpoint(), LEFT, buff=0.2)
        label_b = Text("β").next_to(Line(B, C).get_midpoint(), DOWN, buff=0.2)
        label_c = Text("γ").next_to(Line(C, A).get_midpoint(), UR, buff=0.2)
        self.play(Write(label_a), run_time=0.5)
        self.play(Write(label_b), run_time=0.5)
        self.play(Write(label_c), run_time=0.5)
        # Group the triangle, labels, and angle marker
        group = VGroup(triangle, label_A, label_B, label_C, label_a, label_b, label_c, right_angle_marker)
        self.next_slide()
        # Shrink the triangle and labels with respect to point A
        self.play(group.animate.scale(0.7, about_point=B))
        Hmitono = Text(r"Ο λόγος που σχηματίζεται, αν διαιρέσουμε την " r"απέναντι κάθετη" r" πλευρά", font_size=25).shift(UP * 3)
        Hmitono1 = Text(r"μίας οξείας γωνίας ω ενός ορθογωνίου τριγώνου με την " r"υποτείνουσα,", font_size=25).shift(UP * 2.5)
        Hmitono2 = Text(r"είναι πάντοτε σταθερός και λέγεται " r"ημίτονο " r"της γωνίας ω", font_size=25).shift(UP * 2)
        Hmitono2[30:37].set_color(YELLOW)
        Hmitono1[44:55].set_color(RED)
        Hmitono[38:52].set_color(BLUE)
        self.play(Write(Hmitono))
        self.play(Write(Hmitono1))
        self.play(Write(Hmitono2))
        # Wait for a while
        self.next_slide()

        # Highlight and isolate important words
        important_words = VGroup(
            Hmitono2[30:37],
            Hmitono1[44:55],
            Hmitono[38:52]
        )
        # Create a group animation
        animations = AnimationGroup(
            Hmitono.animate.set_opacity(0),
            Hmitono1.animate.set_opacity(0),
            Hmitono2.animate.set_opacity(0),
            *[word.animate.set_opacity(1).scale(1.5) for word in important_words],
            lag_ratio=0.0  # Synchronous animation
        )

        # Play the group animation
        self.play(animations)
        # Create the equation manually
        sin_text = Text("ημίτονο", font_size=30, color=YELLOW).shift(UP * 2.5 + LEFT * 2.5)
        equal_sign = Text("=", font_size=30).next_to(sin_text)

        # Create numerator and denominator
        numerator = Text("απέναντι κάθετη", font_size=30, color=BLUE).next_to(equal_sign, RIGHT * 0.7 + UP * 0.3)
        denominator = Text("υποτείνουσα", font_size=30, color=RED).next_to(numerator, DOWN, buff=0.3)

        # Draw the fraction line
        fraction_line = Line(
            numerator.get_bottom(),
            denominator.get_top(),
            color=WHITE
        ).scale(12, about_edge=LEFT).rotate(PI * 0.5)

        # Group equation elements
        equation_group = VGroup(sin_text, numerator, denominator)

        # Animate transformation into the equation
        self.play(
            Transform(important_words, equation_group), run_time=1)
        self.play(
            Write(equal_sign),
            Create(fraction_line)
        )
        groupp = VGroup(equation_group, equal_sign, fraction_line)
        self.play(Circumscribe(groupp))
        self.next_slide()


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
