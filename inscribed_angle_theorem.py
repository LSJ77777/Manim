from manim import *
import numpy as np

class InscribedAngleTheorem(Scene):
    def construct(self):
        # 创建基本图形
        circle = Circle(radius=2, color=GREEN)  # 修改为绿色
        center = Dot(ORIGIN, color=RED)  # 修改为红色
        
        # 创建固定的两点A和B（弧的端点）
        angle_a = 0  # A点在最右边
        angle_b = 5*PI/4  # B点在左下方
        point_a = circle.point_at_angle(angle_a)
        point_b = circle.point_at_angle(angle_b)
        dot_a = Dot(point_a, color=BLUE_B)
        dot_b = Dot(point_b, color=BLUE_B)
        
        # 创建C点，固定在左上方
        angle_c = 3*PI/4  # C点在左上方
        point_c = circle.point_at_angle(angle_c)
        dot_c = Dot(point_c, color=BLUE_B, fill_opacity=0)  # 初始透明
        
        # 创建标签，C点标签初始不显示
        labels = VGroup(
            Text("A", font="SimSun").scale(0.6).next_to(dot_a, RIGHT, buff=0.1),
            Text("B", font="SimSun").scale(0.6).next_to(dot_b, DL, buff=0.1),
            Text("C", font="SimSun").scale(0.6).next_to(dot_c, UL, buff=0.1).set_opacity(0),  # 初始透明
            Text("O", font="SimSun").scale(0.6).next_to(center, DL, buff=0.1)
        )

        # 创建连线，AC和BC初始不显示
        lines = VGroup(
            Line(ORIGIN, point_a, color=WHITE),
            Line(ORIGIN, point_b, color=WHITE),
            Line(point_a, point_c, color=BLUE_B, stroke_opacity=0),  # 初始透明
            Line(point_c, point_b, color=BLUE_B, stroke_opacity=0)   # 初始透明
        )

        # 创建圆心角和圆周角标记
        central_angle = Arc(
            radius=0.5,
            angle=angle_between_vectors(
                point_b - ORIGIN,
                point_a - ORIGIN
            ),
            start_angle=angle_of_vector(point_b - ORIGIN),
            color=RED,
            stroke_width=3
        )
        
        inscribed_angle = Arc(
            radius=0.4,
            angle=angle_between_vectors(
                point_b - point_c,
                point_a - point_c
            ),
            start_angle=angle_of_vector(point_b - point_c),
            color=RED,
            arc_center=point_c,
            stroke_opacity=0  # 初始透明
        )

        # 添加角度标记文字
        angle_labels = VGroup(
            Text("∠AOB", font="SimSun", color=RED).scale(0.6),
            Text("∠ACB", font="SimSun", color=RED).scale(0.6).set_opacity(0)  # 初始透明
        )
        
        # 调整角度标记文字位置
        angle_labels[0].next_to(central_angle, UR, buff=0.1)
        angle_labels[1].next_to(inscribed_angle, UR, buff=0.1)

        # 创建标签，进一步调整位置
        labels = VGroup(
            Text("A", font="SimSun").scale(0.6).next_to(dot_a, RIGHT, buff=0.1),
            Text("B", font="SimSun").scale(0.6).next_to(dot_b, DL, buff=0.1),
            Text("C", font="SimSun").scale(0.6).next_to(dot_c, UL, buff=0.1),
            Text("O", font="SimSun").scale(0.6).next_to(center, DL, buff=0.1)
        )

        # 添加说明文字
        title = Text("圆周角定理", font="SimSun", color=BLUE_A).scale(0.8).to_edge(UP)
        
        explanation = VGroup(
            Text("定理内容：", font="SimSun", color=YELLOW_A).scale(0.6),
            Text("圆周角∠ACB等于圆心角∠AOB的一半", font="SimSun").scale(0.5),
            Text("同一弧所对的圆周角相等", font="SimSun").scale(0.5),
            Text("半圆所对的圆周角是直角", font="SimSun").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        explanation.to_edge(LEFT, buff=0.5).shift(UP * 1.5)
        
        # 添加角度标记说明
        angle_legend = VGroup(
            Text("角度说明：", font="SimSun", color=YELLOW_A).scale(0.6),
            VGroup(
                Text("圆心角", font="SimSun", color=RED).scale(0.5),
                Text("∠AOB", font="SimSun", color=RED).scale(0.5)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("圆周角", font="SimSun", color=RED).scale(0.5),
                Text("∠ACB", font="SimSun", color=RED).scale(0.5)
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        angle_legend.next_to(explanation, DOWN, buff=0.5)

        # 计算角度值
        def calculate_angles(a_pos, b_pos, c_pos=None):
            # 计算圆心角，确保是正值
            angle = angle_between_vectors(b_pos - ORIGIN, a_pos - ORIGIN)
            if angle < 0:
                angle += TAU
            central_deg = int(angle * 180 / PI)
            
            # 圆周角严格等于圆心角的一半
            inscribed_deg = central_deg / 2
                
            return central_deg, inscribed_deg

        # 动态更新函数
        def update_point_c(c_angle, a_angle):
            # 更新A点位置
            new_a = circle.point_at_angle(a_angle)
            # 更新C点位置
            new_c = circle.point_at_angle(c_angle)
            
            # 创建弧AB的标注
            arc_ab = self.create_arc_chord_labels(
                ORIGIN, 
                2.3,  # 稍大于圆的半径
                angle_between_vectors(point_b - ORIGIN, new_a - ORIGIN),
                angle_of_vector(point_b - ORIGIN)
            )
            
            # 创建弦AB的标注
            chord_mid = (new_a + point_b) / 2
            chord_label = Text("弦", font="SimSun", color=BLUE_B).scale(0.4)
            chord_label.next_to(chord_mid, DOWN, buff=0.1)
            
            new_lines = VGroup(
                Line(ORIGIN, new_a, color=WHITE),      # OA线段
                Line(ORIGIN, point_b, color=WHITE),    # OB线段
                Line(new_a, new_c, color=BLUE_B),      # AC线段
                Line(new_c, point_b, color=BLUE_B)     # BC线段
            )
            
            # 计算圆心角
            central_angle_value = angle_between_vectors(point_b - ORIGIN, new_a - ORIGIN)
            if central_angle_value < 0:
                central_angle_value += TAU
            
            # 更新圆心角
            new_central = Arc(
                radius=0.5,
                angle=central_angle_value,
                start_angle=angle_of_vector(point_b - ORIGIN),
                color=RED
            )
            
            # 圆周角是圆心角的一半
            inscribed_angle_value = central_angle_value / 2
            
            # 更新圆周角
            new_inscribed = Arc(
                radius=0.4,
                angle=inscribed_angle_value,
                start_angle=angle_of_vector(point_b - new_c),
                color=RED,
                arc_center=new_c
            )
            
            # 计算角度值（保留一位小数）
            new_central_deg = int(central_angle_value * 180 / PI)
            new_inscribed_deg = round(new_central_deg / 2, 1)  # 保留一位小数
            
            # 更新角度标记文字位置
            new_angle_labels = VGroup(
                Text("∠AOB", font="SimSun", color=RED).scale(0.6),
                Text("∠ACB", font="SimSun", color=RED).scale(0.6)
            )
            new_angle_labels[0].next_to(new_central, UR, buff=0.1)
            new_angle_labels[1].next_to(new_inscribed, UR, buff=0.1)
            
            return new_a, new_c, new_lines, new_central, new_inscribed, new_angle_labels, new_central_deg, new_inscribed_deg, arc_ab, chord_label

        # 初始角度值
        central_angle_deg, inscribed_angle_deg = calculate_angles(point_a, point_b)
        
        # 显示基本图形
        self.play(Write(title))
        self.wait(0.5)
        
        self.play(
            Create(circle),
            Create(center),
            Write(labels[3]),  # O点标签
            run_time=1.5
        )
        self.wait(0.5)
        
        # 显示A和B点
        self.play(
            Create(VGroup(dot_a, dot_b)),
            Write(VGroup(labels[0], labels[1])),  # A和B点标签
            run_time=1.5
        )
        self.wait(0.5)
        
        # 创建初始弧和弦的标注
        initial_arc = self.create_arc_chord_labels(
            ORIGIN, 
            2.3,
            angle_between_vectors(point_b - ORIGIN, point_a - ORIGIN),
            angle_of_vector(point_b - ORIGIN)
        )
        initial_chord_label = Text("弧", font="SimSun", color=BLUE_B).scale(0.4)
        initial_chord_label.next_to((point_a + point_b)/2, DOWN, buff=0.1)
        
        # 显示OA、OB线段、圆心角和标注
        self.play(
            Create(VGroup(lines[0], lines[1])),
            Create(central_angle),
            Write(angle_labels[0]),  # 显示∠AOB标记
            Create(initial_arc),
            Write(initial_chord_label),
            run_time=1.5
        )
        self.wait(0.5)
        
        # 显示C点及其相关元素
        self.play(
            dot_c.animate.set_fill_opacity(1),
            labels[2].animate.set_opacity(1),
            lines[2].animate.set_stroke_opacity(1),
            lines[3].animate.set_stroke_opacity(1),
            Create(inscribed_angle),
            Write(angle_labels[1]),  # 显示∠ACB标记
            run_time=1.5
        )
        
        # 显示说明文字
        self.play(Write(explanation))
        self.play(Write(angle_legend))
        
        # A点和C点的动画
        # A点从0移动到-PI/2，减少移动次数
        for i in range(10):  # 10次
            a_angle = -i * PI / 20  # 调整步长以匹配新的次数
            # 计算C点的新位置（在A和B之间）
            c_angle = (a_angle + angle_b) / 2
            
            new_a, new_c, new_lines, new_central, new_inscribed, new_angle_labels, new_central_deg, new_inscribed_deg, arc_ab, chord_label = update_point_c(c_angle, a_angle)
            
            new_angle_values = VGroup(
                Text(f"∠AOB={new_central_deg}°", font="SimSun", color=RED).scale(0.6),
                Text(f"∠ACB={new_inscribed_deg}°", font="SimSun", color=RED).scale(0.6)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            new_angle_values.to_edge(RIGHT, buff=0.5).shift(UP * 1.5)
            
            # 如果是第一次循环，创建角度值显示
            if i == 0:
                self.play(Create(new_angle_values))
                angle_values = new_angle_values
            else:
                # 后续循环使用Transform更新角度值，增加动画时间使移动更平滑
                self.play(
                    dot_a.animate.move_to(new_a),
                    dot_c.animate.move_to(new_c),
                    labels[0].animate.next_to(new_a, RIGHT, buff=0.1),
                    labels[2].animate.next_to(new_c, UL, buff=0.1),
                    Transform(lines, new_lines),
                    Transform(central_angle, new_central),
                    Transform(inscribed_angle, new_inscribed),
                    Transform(angle_labels, new_angle_labels),
                    Transform(angle_values, new_angle_values),
                    Transform(initial_arc, arc_ab),
                    Transform(initial_chord_label, chord_label),
                    run_time=0.8  # 增加动画时间，使移动更平滑
                )
                self.wait(0.2)  # 增加等待时间，让用户更容易观察

        self.wait(1)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        
        # 推理标题
        self.proof_title = Text("圆周角定理的推论", font="SimSun", color=BLUE_A).scale(0.8).to_edge(UP)
        self.play(Write(self.proof_title))
        
        # 创建推论一的文字说明
        proof1_group = self.create_proof1_text()
        
        # 创建基本圆形设置
        demo_circle, demo_center, demo_o_label, circle_config = self.create_demo_circle_setup()
        
        # 创建点和标签
        points, dots, labels, lines, angles, center_dot = self.create_points_and_labels(demo_circle, circle_config)
        
        # 执行动画
        self.play(Write(proof1_group))
        self.play(Create(demo_circle))
        self.play(Create(center_dot))
        self.play(Create(dots))
        self.play(Write(labels))
        
        # 分步创建线段
        self.play(Create(lines[0]))  # BC线段
        self.play(Create(lines[1]))  # AD线段
        self.play(Create(lines[2]))  # BD线段
        self.play(Create(lines[3]))  # AC线段
        
        self.play(Create(angles))
        
        # 修改角度值显示为∠BDA和∠BCD
        angle_text = VGroup(
            Text("∠BDA = ∠BCD", font="SimSun", color=WHITE).scale(0.5)
        ).next_to(demo_circle, DOWN, buff=0.5)
        
        self.play(Write(angle_text))
        
        # 添加动态演示
        self.demonstrate_angle_equality(demo_circle, points, dots, labels, lines, angles, angle_text)
        
        self.wait(1)
        
        # 清除推理一的图示
        demo_group1 = VGroup(
            demo_circle, 
            demo_center, 
            demo_o_label, 
            dots, 
            labels, 
            lines,
            angles,
            angle_text
        )
        self.play(FadeOut(demo_group1))
        
        self.wait(1)
        # 清除除了标题外的所有内容
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.proof_title]
        )
        
        # 推理二
        proof2 = VGroup(
            Text("推论二：", font="SimSun", color=YELLOW_A).scale(0.6),
            Text("半圆所对的圆周角是直角", font="SimSun").scale(0.5),
            Text("直角所对的弧是半圆", font="SimSun").scale(0.5),
            Text("所对的弦是直径", font="SimSun").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        proof2_explanation = VGroup(
            Text("证明：", font="SimSun", color=WHITE).scale(0.5),
            Text("半圆对应的圆心角是180°", font="SimSun").scale(0.4),
            Text("所以圆周角是90°（直角）", font="SimSun").scale(0.4)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        proof2_group = VGroup(proof2, proof2_explanation).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        proof2_group.next_to(self.proof_title, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        
        # 推理二的动态演示
        demo_circle2 = Circle(radius=2, color=GREEN).shift(RIGHT * 3)
        demo_center2 = Dot(demo_circle2.get_center(), color=RED)
        demo_o_label2 = Text("O", font="SimSun").scale(0.4).next_to(demo_center2, DL, buff=0.1)
        
        # 创建直径的两个端点
        diameter_start = demo_circle2.point_at_angle(PI)  # A点
        diameter_end = demo_circle2.point_at_angle(0)    # B点
        
        diameter_dots = VGroup(
            Dot(diameter_start, color=BLUE_B),
            Dot(diameter_end, color=BLUE_B)
        )
        
        diameter_labels = VGroup(
            Text("A", font="SimSun").scale(0.4).next_to(diameter_start, LEFT),
            Text("B", font="SimSun").scale(0.4).next_to(diameter_end, RIGHT)
        )
        
        diameter_line = Line(diameter_start, diameter_end, color=BLUE_B)
        
        # 创建一个动点P和其连线
        point_p = demo_circle2.point_at_angle(PI/4)
        dot_p = Dot(point_p, color=BLUE_B)
        p_label = Text("P", font="SimSun").scale(0.4).next_to(dot_p, UP)
        
        p_lines = VGroup(
            Line(diameter_start, point_p, color=BLUE_B),
            Line(point_p, diameter_end, color=BLUE_B)
        )
        
        # 显示直角符号
        right_angle = RightAngle(
            Line(point_p, diameter_start),
            Line(point_p, diameter_end),
            length=0.2,
            color=RED
        )
        
        # 显示基本元素
        self.play(
            Write(proof2_group),
            Create(demo_circle2),
            Create(demo_center2),
            Write(demo_o_label2),
            Create(diameter_dots),
            Write(diameter_labels),
            Create(diameter_line)
        )
        
        self.play(
            Create(dot_p),
            Write(p_label),
            Create(p_lines),
            Create(right_angle)
        )
        
        # 添加动态演示
        self.demonstrate_semicircle_right_angle(
            demo_circle2, 
            diameter_start, 
            diameter_end, 
            dot_p, 
            p_label, 
            p_lines, 
            right_angle
        )
        
        self.wait(1)
        
        # 清除除了标题外的所有内容
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != self.proof_title]
        )
        
        # 推理三
        proof3 = VGroup(
            Text("推论三：", font="SimSun", color=YELLOW_A).scale(0.6),
            Text("若三角形一边的中线等于这边的一半，", font="SimSun").scale(0.5),
            Text("那么这个三角形是直角三角形", font="SimSun").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        proof3_explanation = VGroup(
            Text("证明：", font="SimSun", color=WHITE).scale(0.5),
            Text("将中线作为半径画圆，原三角形的顶点在圆上", font="SimSun").scale(0.4),
            Text("该边成为直径，由推论二可知对应的角是直角", font="SimSun").scale(0.4)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        proof3_group = VGroup(proof3, proof3_explanation).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        proof3_group.next_to(self.proof_title, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        
        # 推理三的动态演示
        demo_circle3 = Circle(radius=2, color=GREEN).shift(RIGHT * 3)
        demo_center3 = Dot(demo_circle3.get_center(), color=RED)
        center_label = Text("O", font="SimSun").scale(0.4).next_to(demo_center3, DL, buff=0.1)
        
        # 创建三角形的顶点
        # B和A是直径的两端点，C在圆上
        angle_b = PI        # B点在最左边
        angle_a = 0         # A点在最右边
        angle_c = PI/2      # C点在最上方
        
        triangle_points = [
            demo_circle3.point_at_angle(angle_b),     # B点（左边）
            demo_circle3.point_at_angle(angle_a),     # A点（右边）
            demo_circle3.point_at_angle(angle_c)      # C点（上方）
        ]
        
        # 圆心O（BA的中点）
        midpoint = demo_circle3.get_center()
        
        # 创建三角形和点
        triangle_dots = VGroup(*[Dot(point, color=BLUE_B) for point in triangle_points])
        triangle_labels = VGroup(
            Text("B", font="SimSun").scale(0.4).next_to(triangle_points[0], LEFT, buff=0.1),
            Text("A", font="SimSun").scale(0.4).next_to(triangle_points[1], RIGHT, buff=0.1),
            Text("C", font="SimSun").scale(0.4).next_to(triangle_points[2], UP, buff=0.1)
        )
        
        # 显示直径BA
        diameter = Line(triangle_points[0], triangle_points[1], color=BLUE_B)
        
        # 显示从C到两端的线段
        c_lines = VGroup(
            Line(triangle_points[2], triangle_points[0], color=BLUE_B),
            Line(triangle_points[2], triangle_points[1], color=BLUE_B)
        )
        
        # 显示中线（从C到O）
        median = Line(triangle_points[2], midpoint, color=RED)
        midpoint_dot = Dot(midpoint, color=RED)
        
        # 添加直角符号
        right_angle = RightAngle(
            Line(triangle_points[2], triangle_points[0]),
            Line(triangle_points[2], triangle_points[1]),
            length=0.2,
            color=RED
        )
        
        # 显示基本元素
        self.play(
            Write(proof3_group),
            Create(demo_circle3),
            Create(demo_center3),
            Write(center_label)
        )
        
        # 显示直径BA和点
        self.play(
            Create(diameter),
            Create(triangle_dots),
            Write(triangle_labels)
        )
        
        # 显示从C到两端的线段
        self.play(Create(c_lines))
        
        # 显示中线和圆心
        self.play(
            Create(median),
            Create(midpoint_dot)
        )
        
        # 显示直角符号
        self.play(Create(right_angle))
        
        # 添加说明文字
        explanation = VGroup(
            Text("∵ BA是直径，O是BA中点", font="SimSun", color=WHITE).scale(0.4),
            Text("∴ CO ⊥ BA，∠BCA = 90°", font="SimSun", color=WHITE).scale(0.4)
        ).arrange(DOWN, aligned_edge=LEFT)
        explanation.next_to(demo_circle3, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        
        # C点移动的动画
        angles = [PI/3, PI/2, 2*PI/3]  # C点在圆上的不同位置
        
        for angle in angles:
            # 计算C点的新位置
            new_c = demo_circle3.point_at_angle(angle)
            
            # 更新线段
            new_c_lines = VGroup(
                Line(new_c, triangle_points[0], color=BLUE_B),
                Line(new_c, triangle_points[1], color=BLUE_B)
            )
            
            # 更新中线
            new_median = Line(new_c, midpoint, color=RED)
            
            # 更新直角符号
            new_right_angle = RightAngle(
                Line(new_c, triangle_points[0]),
                Line(new_c, triangle_points[1]),
                length=0.2,
                color=RED
            )
            
            # 执行动画
            self.play(
                triangle_dots[2].animate.move_to(new_c),
                triangle_labels[2].animate.next_to(new_c, UP, buff=0.1),
                Transform(c_lines, new_c_lines),
                Transform(median, new_median),
                Transform(right_angle, new_right_angle),
                run_time=1
            )
            
            self.wait(0.5)
        
        # 回到原始位置
        original_c = demo_circle3.point_at_angle(PI/2)
        original_c_lines = VGroup(
            Line(original_c, triangle_points[0], color=BLUE_B),
            Line(original_c, triangle_points[1], color=BLUE_B)
        )
        original_median = Line(original_c, midpoint, color=RED)
        original_right_angle = RightAngle(
            Line(original_c, triangle_points[0]),
            Line(original_c, triangle_points[1]),
            length=0.2,
            color=RED
        )
        
        self.play(
            triangle_dots[2].animate.move_to(original_c),
            triangle_labels[2].animate.next_to(original_c, UP, buff=0.1),
            Transform(c_lines, original_c_lines),
            Transform(median, original_median),
            Transform(right_angle, original_right_angle),
            run_time=1
        )
        
        self.wait(1)
        
        # 最后清除所有内容
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        ) 

    def create_arc_chord_labels(self, arc_center, arc_radius, arc_angle, arc_start_angle, arc_color=RED):
        # 创建弧
        arc = Arc(
            radius=arc_radius,
            angle=arc_angle,
            start_angle=arc_start_angle,
            color=arc_color,
            stroke_width=2
        ).shift(arc_center)
        
        # 计算弧的中点位置
        mid_angle = arc_start_angle + arc_angle/2
        mid_point = arc_center + (arc_radius + 0.3) * np.array([
            np.cos(mid_angle),
            np.sin(mid_angle),
            0
        ])
        
        # 创建弧的标注
        arc_label = Text("⌒", font="SimSun", color=arc_color).scale(0.4)
        arc_label.move_to(mid_point)
        
        return VGroup(arc, arc_label)

    def create_proof1_text(self):
        """创建推论一的文字说明"""
        proof1 = VGroup(
            Text("推论一：", font="SimSun", color=YELLOW_A).scale(0.6),
            Text("同弧或等弧所对的圆周角相等", font="SimSun").scale(0.5),
            Text("相等的圆周角所对的弧是等弧", font="SimSun").scale(0.5)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        
        proof1_explanation = VGroup(
            Text("证明：", font="SimSun", color=WHITE).scale(0.5),
            Text("由圆周角定理可知，圆周角等于圆心角的一半", font="SimSun").scale(0.4),
            Text("所以同弧对应相同的圆心角，因此圆周角相等", font="SimSun").scale(0.4)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        proof1_group = VGroup(proof1, proof1_explanation).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        proof1_group.next_to(self.proof_title, DOWN, buff=0.5).to_edge(LEFT, buff=0.5)
        return proof1_group

    def create_demo_circle_setup(self):
        """创建基本圆形设置"""
        circle_config = {
            "radius": 1.5,
            "color": GREEN,  # 改为绿色以匹配图片
            "shift_amount": RIGHT * 3
        }
        
        demo_circle = Circle(
            radius=circle_config["radius"], 
            color=circle_config["color"]
        ).shift(circle_config["shift_amount"])
        
        demo_center = Dot(demo_circle.get_center(), color=RED)  # 改为红色以匹配图片
        demo_o_label = Text("O", font="SimSun").scale(0.4).next_to(demo_center, DL, buff=0.1)
        
        return demo_circle, demo_center, demo_o_label, circle_config

    def create_points_and_labels(self, demo_circle, circle_config):
        """创建圆上的点和标签，按照图片重新布局"""
        # 修改点的角度位置以精确匹配图片
        angle_a = 0          # A点在最右边
        angle_b = 5*PI/4     # B点在左下方
        angle_c = PI/4       # C点在右上方
        angle_d = 3*PI/4     # D点在左上方
        
        circle_center = demo_circle.get_center()
        radius = circle_config["radius"]
        
        points = {
            "A": circle_center + radius * np.array([np.cos(angle_a), np.sin(angle_a), 0]),
            "B": circle_center + radius * np.array([np.cos(angle_b), np.sin(angle_b), 0]),
            "C": circle_center + radius * np.array([np.cos(angle_c), np.sin(angle_c), 0]),
            "D": circle_center + radius * np.array([np.cos(angle_d), np.sin(angle_d), 0])
        }
        
        # 创建点（使用蓝色）
        dots = VGroup(*[Dot(point, color=BLUE_B) for point in points.values()])
        
        # 创建圆心点（红色）
        center_dot = Dot(circle_center, color=RED)
        
        # 调整标签位置
        labels = VGroup(
            Text("A", font="SimSun", color=WHITE).scale(0.4).next_to(points["A"], RIGHT, buff=0.1),
            Text("B", font="SimSun", color=WHITE).scale(0.4).next_to(points["B"], DL, buff=0.1),
            Text("C", font="SimSun", color=WHITE).scale(0.4).next_to(points["C"], UR, buff=0.1),
            Text("D", font="SimSun", color=WHITE).scale(0.4).next_to(points["D"], UL, buff=0.1),
            Text("O", font="SimSun", color=WHITE).scale(0.4).next_to(circle_center, DL, buff=0.1)
        )
        
        # 创建所有线段（蓝色）
        lines = VGroup(
            Line(points["B"], points["C"], color=BLUE_B),  # BC线段
            Line(points["A"], points["D"], color=BLUE_B),  # AD线段
            Line(points["B"], points["D"], color=BLUE_B),  # BD线段
            Line(points["A"], points["C"], color=BLUE_B)   # AC线段
        )
        
        # 创建角度标记（红色）
        # 修改角度标记为∠BDA和∠BCD
        angle_c = Arc(
            radius=0.2,
            angle=angle_between_vectors(
                points["B"] - points["C"],
                points["D"] - points["C"]
            ),
            start_angle=angle_of_vector(points["B"] - points["C"]),
            color=RED,
            arc_center=points["C"]
        )
        
        angle_d = Arc(
            radius=0.2,
            angle=angle_between_vectors(
                points["B"] - points["D"],
                points["A"] - points["D"]
            ),
            start_angle=angle_of_vector(points["B"] - points["D"]),
            color=RED,
            arc_center=points["D"]
        )
        
        angles = VGroup(angle_c, angle_d)
        
        return points, dots, labels, lines, angles, center_dot 

    def demonstrate_angle_equality(self, demo_circle, points, dots, labels, lines, angles, angle_text):
        """演示C和D点移动时角度相等"""
        # 创建新的位置
        radius = demo_circle.radius
        circle_center = demo_circle.get_center()
        
        # C点移动到新位置
        new_angle_c = PI/2  # 移动到顶部
        new_c = circle_center + radius * np.array([np.cos(new_angle_c), np.sin(new_angle_c), 0])
        
        # D点移动到新位置
        new_angle_d = PI  # 移动到左边
        new_d = circle_center + radius * np.array([np.cos(new_angle_d), np.sin(new_angle_d), 0])
        
        # 更新线段
        new_lines = VGroup(
            Line(points["B"], new_c, color=BLUE_B),  # BC线段
            Line(points["A"], new_d, color=BLUE_B),  # AD线段
            Line(points["B"], new_d, color=BLUE_B),  # BD线段
            Line(points["A"], new_c, color=BLUE_B)   # AC线段
        )
        
        # 更新角度标记
        new_angle_c = Arc(
            radius=0.2,
            angle=angle_between_vectors(
                points["B"] - new_c,
                new_d - new_c
            ),
            start_angle=angle_of_vector(points["B"] - new_c),
            color=RED,
            arc_center=new_c
        )
        
        new_angle_d = Arc(
            radius=0.2,
            angle=angle_between_vectors(
                points["B"] - new_d,
                points["A"] - new_d
            ),
            start_angle=angle_of_vector(points["B"] - new_d),
            color=RED,
            arc_center=new_d
        )
        
        new_angles = VGroup(new_angle_c, new_angle_d)
        
        # 执行动画
        self.play(
            dots[2].animate.move_to(new_c),
            dots[3].animate.move_to(new_d),
            labels[2].animate.next_to(new_c, UP, buff=0.1),
            labels[3].animate.next_to(new_d, LEFT, buff=0.1),
            Transform(lines, new_lines),
            Transform(angles, new_angles),
            run_time=2
        )
        self.wait(0.5)
        
        # 移回原位
        original_angle_c = Arc(
            radius=0.2,
            angle=angle_between_vectors(
                points["B"] - points["C"],
                points["D"] - points["C"]
            ),
            start_angle=angle_of_vector(points["B"] - points["C"]),
            color=RED,
            arc_center=points["C"]
        )
        
        original_angle_d = Arc(
            radius=0.2,
            angle=angle_between_vectors(
                points["B"] - points["D"],
                points["A"] - points["D"]
            ),
            start_angle=angle_of_vector(points["B"] - points["D"]),
            color=RED,
            arc_center=points["D"]
        )
        
        original_angles = VGroup(original_angle_c, original_angle_d)
        
        self.play(
            dots[2].animate.move_to(points["C"]),
            dots[3].animate.move_to(points["D"]),
            labels[2].animate.next_to(points["C"], UR, buff=0.1),
            labels[3].animate.next_to(points["D"], UL, buff=0.1),
            Transform(lines, VGroup(*[
                Line(points["B"], points["C"], color=BLUE_B),
                Line(points["A"], points["D"], color=BLUE_B),
                Line(points["B"], points["D"], color=BLUE_B),
                Line(points["A"], points["C"], color=BLUE_B)
            ])),
            Transform(angles, original_angles),
            run_time=2
        ) 

    def demonstrate_semicircle_right_angle(self, circle, start, end, dot_p, p_label, p_lines, right_angle):
        """演示半圆中的直角性质"""
        # 创建几个不同的位置进行动画演示（避开端点）
        angles = [PI/6, PI/3, PI/2, 2*PI/3, 5*PI/6]  # 在半圆上选择几个位置，避开0和PI
        
        for angle in angles:
            # 计算新位置（确保在圆上）
            new_p = circle.point_at_angle(angle)
            
            # 创建新的连线
            new_lines = VGroup(
                Line(start, new_p, color=BLUE_B),
                Line(new_p, end, color=BLUE_B)
            )
            
            # 创建新的直角符号
            new_right_angle = RightAngle(
                Line(new_p, start),
                Line(new_p, end),
                length=0.2,
                color=RED
            )
            
            # 计算标签的位置（根据点的位置调整）
            if angle < PI/2:
                label_direction = UP + RIGHT
            elif angle > PI/2:
                label_direction = UP + LEFT
            else:
                label_direction = UP
            
            # 执行动画
            self.play(
                dot_p.animate.move_to(new_p),
                p_label.animate.next_to(new_p, label_direction, buff=0.1),
                Transform(p_lines, new_lines),
                Transform(right_angle, new_right_angle),
                run_time=1.5
            )
            self.wait(0.5)
        
        # 最后回到原始位置（PI/4）
        original_p = circle.point_at_angle(PI/4)
        original_lines = VGroup(
            Line(start, original_p, color=BLUE_B),
            Line(original_p, end, color=BLUE_B)
        )
        original_right_angle = RightAngle(
            Line(original_p, start),
            Line(original_p, end),
            length=0.2,
            color=RED
        )
        
        self.play(
            dot_p.animate.move_to(original_p),
            p_label.animate.next_to(original_p, UP + RIGHT, buff=0.1),
            Transform(p_lines, original_lines),
            Transform(right_angle, original_right_angle),
            run_time=1
        ) 

# manim -pqh inscribed_angle_theorem.py InscribedAngleTheorem