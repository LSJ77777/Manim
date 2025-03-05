from manim import *
import numpy as np

class CentralAngleTheorem(Scene):
    def construct(self):
        # 创建基本图形
        circle = Circle(radius=2, color=WHITE)
        center = Dot(ORIGIN, color=WHITE)
        
        # 创建两对点，展示两个相等的圆心角
        angle1 = PI/3  # 60度
        angle2 = 2*PI/3  # 120度
        
        # 第一对点
        point_a = circle.point_at_angle(angle1)
        point_b = circle.point_at_angle(angle1 + PI/3)  # 额外60度
        dot_a = Dot(point_a, color=YELLOW)
        dot_b = Dot(point_b, color=YELLOW)
        
        # 第二对点
        point_c = circle.point_at_angle(angle2)
        point_d = circle.point_at_angle(angle2 + PI/3)  # 相同的60度
        dot_c = Dot(point_c, color=RED)
        dot_d = Dot(point_d, color=RED)

        # 创建标签
        labels = VGroup(
            Text("A", font="SimSun").scale(0.6).next_to(dot_a, UP+RIGHT),
            Text("B", font="SimSun").scale(0.6).next_to(dot_b, UP+RIGHT),
            Text("C", font="SimSun").scale(0.6).next_to(dot_c, UP+LEFT),
            Text("D", font="SimSun").scale(0.6).next_to(dot_d, DOWN+LEFT),
            Text("O", font="SimSun").scale(0.6).next_to(center, DOWN+LEFT)
        )

        # 创建连线
        lines = VGroup(
            Line(ORIGIN, point_a, color=WHITE),
            Line(ORIGIN, point_b, color=WHITE),
            Line(ORIGIN, point_c, color=WHITE),
            Line(ORIGIN, point_d, color=WHITE),
            Line(point_a, point_b, color=YELLOW),
            Line(point_c, point_d, color=RED)
        )

        # 创建角度标记
        angle_aob = Arc(
            radius=0.5,
            angle=PI/3,
            start_angle=angle1,
            color=YELLOW
        )
        angle_cod = Arc(
            radius=0.5,
            angle=PI/3,
            start_angle=angle2,
            color=RED
        )

        # 创建弦心距（垂直平分线）
        def get_perpendicular_bisector(p1, p2, color):
            mid_point = (p1 + p2) / 2
            direction = normalize(p2 - p1)
            perpendicular = rotate_vector(direction, PI/2)
            # 计算中点到圆心的向量
            to_center = ORIGIN - mid_point
            # 调整虚线位置，使其从中点延伸到圆心
            return VGroup(
                DashedLine(
                    mid_point,  # 从中点开始
                    ORIGIN,     # 延伸到圆心
                    color=color,
                    dash_length=0.1,
                    dashed_ratio=0.5,
                ),
                # 添加中点标记
                Dot(mid_point, color=color)
            )

        perp_group1 = get_perpendicular_bisector(point_a, point_b, YELLOW)
        perp_group2 = get_perpendicular_bisector(point_c, point_d, RED)
        
        # 添加 E 和 F 点的标签
        mid_point1 = (point_a + point_b) / 2
        mid_point2 = (point_c + point_d) / 2
        label_e = Text("E", font="SimSun").scale(0.6).next_to(mid_point1, RIGHT)
        label_f = Text("F", font="SimSun").scale(0.6).next_to(mid_point2, LEFT)

        # 添加说明文字
        title = Text("圆心角定理", font="SimSun", color=BLUE).scale(0.8).to_edge(UP)
        theorem = VGroup(
            Text("在圆中，相等的圆心角：", font="SimSun"),
            Text("1. 所对的弦相等", font="SimSun"),
            Text("2. 所对的弧相等", font="SimSun"),
            Text("3. 弦心距相等", font="SimSun")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.6).to_edge(RIGHT)

        # 动画展示
        self.play(Write(title), run_time=2)
        self.wait(1)

        self.play(
            Create(circle), 
            Create(center), 
            Write(labels[4]), 
            run_time=2
        )
        self.wait(0.5)

        self.play(
            Create(VGroup(dot_a, dot_b, dot_c, dot_d)),
            Write(VGroup(*labels[:4])),
            run_time=2
        )
        self.wait(0.5)

        self.play(Create(lines), run_time=2)
        self.wait(0.5)

        self.play(
            Create(angle_aob), 
            Create(angle_cod), 
            run_time=1.5
        )
        self.wait(0.5)

        self.play(Write(theorem[0]), run_time=1.5)
        self.wait(1)

        # 展示弦相等
        self.play(
            Indicate(lines[4]),
            Indicate(lines[5]),
            Write(theorem[1]),
            run_time=2
        )
        self.wait(1)

        # 展示弧相等
        arc1 = Arc(radius=2, angle=PI/3, start_angle=angle1, color=YELLOW)
        arc2 = Arc(radius=2, angle=PI/3, start_angle=angle2, color=RED)
        self.play(
            Create(arc1),
            Create(arc2),
            Write(theorem[2]),
            run_time=2
        )
        self.wait(1)

        # 展示弦心距
        self.play(
            Create(perp_group1),
            Create(perp_group2),
            Write(VGroup(label_e, label_f)),
            Write(theorem[3]),
            run_time=2
        )
        self.wait(1)

        # 添加角度标记文字
        angle_labels = VGroup(
            Text("∠AOB = ∠COD", font="SimSun", color=YELLOW),
            Text("AB = CD", font="SimSun", color=WHITE),
            Text("弧AB = 弧CD", font="SimSun", color=WHITE),
            Text("OE = OF", font="SimSun", color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.5).to_edge(DOWN)

        self.play(Write(angle_labels), run_time=2)
        self.wait(2) 

# manim -pqh central_angle_theorem.py CentralAngleTheorem