from manim import *
from manim_slides import Slide


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
                # Update function to move the dot and update the lines
        def update_dot_and_lines(obj):
            angle = dot_angle_tracker.get_value()
            dot.move_to(c1.point_at_angle(np.radians(angle)))

            # Update line_to_center to connect from center to dot
            line_to_center.put_start_and_end_on(axes.c2p(0, 0), dot.get_center())

            # Update line_to_x_axis to point from dot to x-axis (cosine)
            x_projection_point = dot.get_center()[0] * RIGHT
            line_to_x_axis.put_start_and_end_on(dot.get_center(), x_projection_point)

            # Update line_to_y_axis to point from dot to y-axis (sine)
            y_projection_point = dot.get_center()[1] * UP
            line_to_y_axis.put_start_and_end_on(dot.get_center(), y_projection_point)

            # Update angle arc and theta label
            angle_arc.become(Arc(radius=0.5, angle=(angle % 360) * DEGREES, arc_center=c1.get_center(), color=WHITE))

        # Displaying the mathematical expressions
        im = MathTex(r"i^i = e^{-\frac{\pi}{2}}").scale(2)
        im.set_color_by_gradient(BLUE, LIGHT_PINK, RED)
        giati = Text("Why", line_spacing=1, font="Times New Roman", font_size=35).shift(UP * 1)
        self.play(Write(im), run_time=3)
        self.next_slide()
        self.play(Write(giati))
        self.next_slide()
        self.play(im.animate.shift(UP * 6.5), FadeOut(giati))
        self.next_slide()

        # More text and mathematical formula
        typos = Text("Euler form", line_spacing=1, font="Times New Roman", font_size=35).shift(UP * 1)
        fo = MathTex(r"e^{i\theta}", r"=", r"\cos(\theta)", r"+", r"i\sin(\theta)").scale(1)
        fo[2][4].set_color(YELLOW)
        fo[4][5].set_color(YELLOW)
        fo[0][2].set_color(YELLOW)
        fo2 = MathTex(r"e^{i\frac{\pi}{2}}", r"=", r"\cos(\frac{\pi}{2})", r"+", r"i\sin(\frac{\pi}{2})").scale(1).shift (UP * 4)
        fo3 = MathTex(r"e^{i\frac{\pi}{2}}", r"=", r"0", r"+", r"i\sin(\frac{\pi}{2})").scale(1).shift (UP * 4)
        fo4 = MathTex(r"e^{i\frac{\pi}{2}}", r"=", r"0", r"+", r"i 1").scale(1).shift (UP * 4)
        fo5 = MathTex(r"e^{i\frac{\pi}{2}}", r"=", r"i").scale(1).shift (UP * 4)
        fo2[2][4:7].set_color(YELLOW)
        fo2[4][5:8].set_color(YELLOW)
        fo2[0][2:6].set_color(YELLOW)
        fo2[2][0:4].set_color(RED)
        fo2[2][7].set_color(RED)
        fo2[4][1:5].set_color(BLUE)
        fo2[4][8].set_color(BLUE)
        self.play(Create(typos))
        self.next_slide()
        self.play(Write(fo))
        self.next_slide()   
        self.play(typos.animate.shift(UP * 4), fo.animate.shift(UP * 4))
        self.next_slide()
        
        # Creating axes and a circle
        axes = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5], x_length=6, y_length=6, axis_config={'tip_shape': StealthTip})
        labels = axes.get_axis_labels(Tex("Re").scale(1), Tex("Im").scale(1))
        c1 = Circle(radius=2, color=WHITE)
        uni = MathTex(r"1").shift(RIGHT * 2.3, DOWN * 0.4).scale(0.8)
        un = MathTex(r"i").shift(UP * 2.3, RIGHT * 0.3).scale(0.8)
        uni2 = MathTex(r"-1").shift(LEFT * 2.3, DOWN * 0.4).scale(0.8)
        un2 = MathTex(r"-i").shift(DOWN * 2.3, RIGHT * 0.3).scale(0.8)

        self.play(Write(axes), Write(labels), Write(uni), Write(un), Write(uni2), Write(un2))
        self.next_slide()
        self.play(Create(c1))
        self.next_slide()
        # Adding a dot inside the circle and lines to the center, x-axis, and y-axis
        dot = Dot(color=WHITE)
        dot.move_to(c1.point_at_angle(np.radians(45)))  # You can customize the color and size of the dot
        dot_angle_tracker = ValueTracker(45)  # Tracker for the angle in degrees, starting from 45 degrees

        # Define line_to_center with animation from center to dot
        line_to_center = Arrow(axes.c2p(0, 0), c1.point_at_angle(np.radians(45)), color=WHITE)
        line_to_center.put_start_and_end_on(axes.c2p(0, 0), dot.get_center())

        # Define line_to_x_axis with animation from dot to x-axis (cosine)
        x_projection_point = c1.point_at_angle(np.radians(45))[0] * RIGHT
        line_to_x_axis = DashedLine(c1.point_at_angle(np.radians(45)), x_projection_point, color=BLUE)

        # Define line_to_y_axis with animation from dot to y-axis (sine)
        y_projection_point = c1.point_at_angle(np.radians(45))[1] * UP
        line_to_y_axis = DashedLine(c1.point_at_angle(np.radians(45)), y_projection_point, color=RED)

        # Label arc for the angle
        angle_arc = Arc(radius=0.5, angle=45 * DEGREES, arc_center=c1.get_center(), color=WHITE)

        # Label for the angle theta
        theta_label = MathTex(r"\theta", color=(YELLOW)).next_to(angle_arc).scale(0.7)
        theta_label2 = MathTex(r"\theta =", r"90^\circ", color=(YELLOW)).shift(UP * 0.5).shift(RIGHT * 1).scale(0.7)
        theta_label3 = MathTex(r"\theta =", r"\frac{\pi}{2}", color=(YELLOW)).shift(UP * 0.5).shift(RIGHT * 1).scale(0.7)

        # Animating the creation of dot, lines, angle arc, and theta label
        self.play(Create(dot))
        self.next_slide()
        self.play(Write(line_to_center))
        self.next_slide()
        self.play(Create(angle_arc), Create(line_to_x_axis), Create(line_to_y_axis))
        self.next_slide()
        # Continuously update the dot and lines' positions based on the tracker
        dot.add_updater(update_dot_and_lines)

        # Adding Animation Group for coloring
        Animations = []
        Animations.append(fo[2][0:4].animate.set_color(RED))
        Animations.append(fo[2][5].animate.set_color(RED))
        Animations.append(fo[4][1:5].animate.set_color(BLUE))
        Animations.append(fo[4][6].animate.set_color(BLUE))

        # Adding Animation Group for fading
        Animations2 = []
        Animations2.append(typos.animate.set_opacity(0))
        Animations2.append(theta_label3.animate.set_opacity(0))
        Animations2.append(labels.animate.set_opacity(0))
        Animations2.append(dot.animate.set_opacity(0))
        Animations2.append(line_to_center.animate.set_opacity(0))
        Animations2.append(line_to_x_axis.animate.set_opacity(0))
        Animations2.append(line_to_y_axis.animate.set_opacity(0))
        Animations2.append(angle_arc.animate.set_opacity(0))
        Animations2.append(c1.animate.set_opacity(0))
        Animations2.append(un.animate.set_opacity(0))
        Animations2.append(un2.animate.set_opacity(0))
        Animations2.append(uni.animate.set_opacity(0))
        Animations2.append(uni2.animate.set_opacity(0))



        # Animating the movement of the dot
        self.play(AnimationGroup(*Animations))
        self.play(dot_angle_tracker.animate.set_value(100),)
        self.play(dot_angle_tracker.animate.set_value(10),)
        self.play(dot_angle_tracker.animate.set_value(30),)
        self.play(Write(theta_label))
        self.play(FadeOut(theta_label))
        self.wait(1)
        self.play(dot_angle_tracker.animate.set_value(90), run_time=3)
        self.play(Write(theta_label2))
        self.wait(0.5)
        self.play(Transform(theta_label2, theta_label3))
        self.wait(0)
        self.play(ReplacementTransform(fo, fo2))
        self.wait(1)
        self.play(ReplacementTransform(fo2, fo3))
        self.play(ReplacementTransform(fo3, fo4))
        self.play(ReplacementTransform(fo4, fo5))
        self.wait(1)
        self.play(AnimationGroup(*Animations2))
        self.wait(1)


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
