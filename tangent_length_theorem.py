from manim import *
import numpy as np

class TangentLengthTheorem(Scene):
    def setup_scene(self):
        # 第一部分：切线长定理
        self.title = Text("切线长定理", font="SimSun", color=BLUE).scale(0.8).to_edge(UP)
        
        self.theorem_content = VGroup(
            Text("切线长定理：", font="SimSun", color=BLUE).scale(0.6),
            Text("从圆外一点引圆的两条切线，它们的切线长相等。", font="SimSun").scale(0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.proof_steps = VGroup(
            Text("证明：", font="SimSun", color=YELLOW_D).scale(0.5),
            Text("1. 连接圆心O与切点A、B", font="SimSun").scale(0.5),
            Text("2. OA ⊥ PA, OB ⊥ PB（切线垂直于半径）", font="SimSun").scale(0.5),
            Text("3. OA = OB = R（半径相等）", font="SimSun").scale(0.5),
            Text("4. ∴ △OAP ≌ △OBP（斜边相等）", font="SimSun").scale(0.5),
            Text("5. ∴ PA = PB（对应边相等）", font="SimSun").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.text_group = VGroup(self.theorem_content, self.proof_steps)\
            .arrange(DOWN, aligned_edge=LEFT, buff=0.5)\
            .to_edge(LEFT, buff=0.5).shift(UP * 0.5)

    def setup_circle(self):
        # 创建基本图形
        self.circle = Circle(radius=1.5, color=GREEN)
        self.circle.shift(RIGHT * 2 + DOWN * 0.5)
        
        # 创建圆心
        self.center = Dot(self.circle.get_center(), color=RED, radius=0.05)
        self.center_label = Text("O", font="SimSun").scale(0.4).next_to(self.center, DR, buff=0.1)

    def setup_points(self):
        # 创建圆外点P
        self.point_p = self.circle.get_center() + np.array([-2, 0, 0])
        self.dot_p = Dot(self.point_p, color=RED, radius=0.05)
        self.p_label = Text("P", font="SimSun").scale(0.4).next_to(self.dot_p, LEFT, buff=0.1)
        
        # 计算切点
        op_length = np.linalg.norm(self.point_p - self.circle.get_center())
        radius = self.circle.radius
        self.angle = np.arccos(radius/op_length)
        op_direction = normalize(self.point_p - self.circle.get_center())
        
        self.tangent_point1 = self.circle.get_center() + radius * rotate_vector(op_direction, self.angle)
        self.tangent_point2 = self.circle.get_center() + radius * rotate_vector(op_direction, -self.angle)
        
        self.dot_t1 = Dot(self.tangent_point1, color=RED, radius=0.05)
        self.dot_t2 = Dot(self.tangent_point2, color=RED, radius=0.05)
        self.t1_label = Text("A", font="SimSun").scale(0.4).next_to(self.dot_t1, DR, buff=0.1)
        self.t2_label = Text("B", font="SimSun").scale(0.4).next_to(self.dot_t2, UR, buff=0.1)

    def setup_lines(self):
        # 创建切线
        self.tangent1 = Line(self.point_p, self.tangent_point1, color=BLUE_D)
        self.tangent2 = Line(self.point_p, self.tangent_point2, color=BLUE_D)
        
        # 创建半径（虚线）
        self.radius1 = DashedLine(self.circle.get_center(), self.tangent_point1, color=RED)
        self.radius2 = DashedLine(self.circle.get_center(), self.tangent_point2, color=RED)
        
        # 创建PO线
        self.po_line = Line(self.point_p, self.circle.get_center(), color=BLUE_D)
        
        # 创建直角符号
        self.right_angle1 = RightAngle(
            self.radius1, self.tangent1,
            length=0.15,
            color=WHITE,
            quadrant=(-1, -1)
        )
        self.right_angle2 = RightAngle(
            self.radius2, self.tangent2,
            length=0.15,
            color=WHITE,
            quadrant=(-1, -1)
        )

    def setup_second_part(self):
        # 第二部分：切线的性质与判定
        self.properties_title = Text("切线的性质与判定", font="SimSun", color=BLUE).scale(0.8).to_edge(UP)
        
        self.properties = VGroup(
            Text("切线的性质：", font="SimSun", color=BLUE).scale(0.6),
            Text("1. 切线与半径垂直", font="SimSun").scale(0.5),
            Text("2. 切点是切线与圆的唯一公共点", font="SimSun").scale(0.5),
            Text("3. 切线是过切点的所有直线中与圆的位置关系最特殊的一条", font="SimSun").scale(0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        self.judgments = VGroup(
            Text("切线的判定：", font="SimSun", color=BLUE).scale(0.6),
            Text("1. 垂直判定：过圆上一点的直线与该点的半径垂直，则此直线是圆的切线", font="SimSun").scale(0.5),
            Text("2. 距离判定：过圆外一点到圆的最短距离是该点到圆的切点的距离", font="SimSun").scale(0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        # 调整文字位置，向左移动并缩小宽度
        self.properties_group = VGroup(self.properties, self.judgments)\
            .arrange(DOWN, aligned_edge=LEFT, buff=0.5)\
            .scale(0.8)\
            .to_edge(LEFT, buff=1.0)

        # 创建第二部分的图形演示，向右移动
        self.circle2 = Circle(radius=1.5, color=GREEN)
        self.circle2.shift(RIGHT * 3.5 + DOWN * 0.5)  # 更靠右的位置
        
        # 创建圆心和标签
        self.center2 = Dot(self.circle2.get_center(), color=RED, radius=0.05)
        self.center_label2 = Text("O", font="SimSun").scale(0.4).next_to(self.center2, DR, buff=0.1)
        
        # 创建切点T
        angle = PI/4
        self.tangent_point2 = self.circle2.point_at_angle(angle)
        self.dot_t2 = Dot(self.tangent_point2, color=RED, radius=0.05)
        self.t_label2 = Text("T", font="SimSun").scale(0.4).next_to(self.dot_t2, UR, buff=0.1)
        
        # 创建半径OT
        self.radius2 = DashedLine(self.circle2.get_center(), self.tangent_point2, color=RED)
        
        # 创建切线
        tangent_direction = rotate_vector(
            self.tangent_point2 - self.circle2.get_center(),
            PI/2
        )
        self.tangent2 = Line(
            self.tangent_point2 - tangent_direction,
            self.tangent_point2 + tangent_direction,
            color=BLUE_D
        )
        
        # 创建直角符号
        self.right_angle2 = RightAngle(
            self.radius2, self.tangent2,
            length=0.15,
            color=WHITE,
            quadrant=(-1, -1)
        )

    def construct(self):
        # 第一部分：切线长定理演示
        self.setup_scene()
        self.setup_circle()
        self.setup_points()
        self.setup_lines()
        
        # 显示标题和定理
        self.play(Write(self.title), run_time=2)
        self.wait(1)
        self.play(Write(self.theorem_content), run_time=2)
        self.wait(1)
        
        # 显示基本图形
        self.play(Create(self.circle), run_time=2)
        self.wait(0.5)
        self.play(
            Create(self.center), 
            Write(self.center_label), 
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Create(self.dot_p), 
            Write(self.p_label), 
            run_time=1.5
        )
        self.wait(1)
        
        # 显示切点和切线
        self.play(
            Create(self.dot_t1), Create(self.dot_t2),
            Write(self.t1_label), Write(self.t2_label),
            run_time=2
        )
        self.wait(1)
        self.play(
            Create(self.tangent1), 
            Create(self.tangent2), 
            run_time=2
        )
        self.wait(1)
        
        # 显示证明步骤
        for i, step in enumerate(self.proof_steps):
            if i == 0:
                self.play(Write(step), run_time=1.5)
                self.wait(1)
            elif i == 1:
                self.play(Write(step), run_time=1.5)
                self.wait(0.5)
                self.play(
                    Create(self.radius1), 
                    Create(self.radius2), 
                    run_time=2
                )
                self.wait(1)
            elif i == 2:
                self.play(Write(step), run_time=1.5)
                self.wait(0.5)
                self.play(
                    Create(self.right_angle1), 
                    Create(self.right_angle2), 
                    run_time=2
                )
                self.wait(1)
            elif i == 3:
                self.play(Write(step), run_time=1.5)
                self.wait(1)
            elif i == 4:
                self.play(Write(step), run_time=1.5)
                self.wait(0.5)
                self.play(Create(self.po_line), run_time=1.5)
                self.wait(1)
            elif i == 5:
                self.play(Write(step), run_time=1.5)
                self.wait(1)
        
        self.wait(3)  # 第一部分结束后多等待
        
        # 清除第一部分内容
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        self.wait(1.5)
        
        # 第二部分：切线的性质与判定
        self.setup_second_part()
        
        # 显示标题和性质
        self.play(Write(self.properties_title), run_time=2)
        self.wait(1)
        self.play(Write(self.properties), run_time=3)
        self.wait(1.5)
        
        # 展示图形演示
        self.play(Create(self.circle2), run_time=2)
        self.wait(0.5)
        self.play(
            Create(self.center2), 
            Write(self.center_label2), 
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Create(self.dot_t2), 
            Write(self.t_label2), 
            run_time=1.5
        )
        self.wait(1)
        
        # 演示切线与半径垂直的性质
        self.play(Create(self.radius2), run_time=1.5)
        self.wait(0.5)
        self.play(Create(self.tangent2), run_time=1.5)
        self.wait(0.5)
        self.play(Create(self.right_angle2), run_time=1.5)
        self.wait(1)
        
        # 强调切点是唯一公共点
        self.play(
            Indicate(self.dot_t2, scale_factor=1.5),
            Flash(self.dot_t2, color=YELLOW, flash_radius=0.3),
            run_time=2
        )
        self.wait(1)
        
        # 显示判定
        self.play(Write(self.judgments), run_time=3)
        self.wait(3) 

# manim -pqh tangent_length_theorem.py TangentLengthTheorem