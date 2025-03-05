from manim import *
import numpy as np


class PerpendicularDiameterTheorem(Scene):
    def construct(self):
        # 创建圆和圆心 (移除圆心的小圆)
        circle = Circle(radius=2, color=RED)
        circle_center = Dot(color=WHITE, radius=0.04)  # 减小圆心大小
        center_label = Text("O", font="SimSun").scale(0.6).next_to(circle_center, DR, buff=0.1)  # 添加O点标记

        # 创建直径
        diameter = Line(LEFT * 2, RIGHT * 2, color=BLUE)

        # 创建动态弦的函数
        def get_chord(t):
            # t 范围从-1.5到1.5，控制E点在直径上的位置
            intersection_point = RIGHT * t
            chord_length = 2 * np.sqrt(4 - t ** 2)  # 根据圆方程计算弦长
            return Line(
                intersection_point + UP * chord_length / 2,
                intersection_point + DOWN * chord_length / 2,
                color=GREEN
            )

        # 初始弦
        chord = get_chord(1)

        # 创建动态点和标签
        def update_points(t):
            intersection_point = RIGHT * t
            chord = get_chord(t)
            point_up = Dot(chord.get_start(), color=YELLOW)
            point_down = Dot(chord.get_end(), color=YELLOW)
            point_intersection = Dot(intersection_point, color=RED)

            # 更新标签位置
            point_a = Text("A", font="SimSun").scale(0.6).next_to(point_up, UP)
            point_b = Text("B", font="SimSun").scale(0.6).next_to(point_down, DOWN)
            point_e = Text("E", font="SimSun").scale(0.6).next_to(point_intersection, RIGHT)

            # 计算长度
            length = np.sqrt(4 - t ** 2)  # AE或BE的长度
            length_text = Text(f"{length:.2f}", font="SimSun").scale(0.5)

            return VGroup(
                chord, point_up, point_down, point_intersection,
                point_a, point_b, point_e,
                length_text.copy().next_to(chord, LEFT).shift(UP * 0.5),
                length_text.copy().next_to(chord, LEFT).shift(DOWN * 0.5)
            )

        # 初始构建
        moving_parts = update_points(1)

        # 添加初始说明文字
        title = Text("垂径定理", font="SimSun", color=BLUE).scale(0.8).to_edge(UP)
        intro_text = VGroup(
            Text("在圆O中，我们将证明：", font="SimSun"),
            Text("当弦AB垂直于直径时，", font="SimSun"),
            Text("E点将弦AB平分", font="SimSun")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.6).to_edge(UP)

        self.add(title)
        self.play(Write(intro_text), run_time=2)  # 增加到2秒
        self.wait(1.5)  # 多等待一会儿
        self.play(FadeOut(intro_text), run_time=1.5)
        self.wait(1)

        # 基础元素动画
        self.play(
            Create(circle), 
            Create(circle_center),
            Write(center_label),  # 添加O点标记的动画
            run_time=2
        )
        self.wait(0.5)
        self.play(Create(diameter), run_time=1.5)
        self.wait(0.5)
        self.play(Create(moving_parts), run_time=2)
        self.wait(1)

        # 添加虚线OA和OB
        def get_radius_lines(t):
            chord = get_chord(t)
            point_up = chord.get_start()
            point_down = chord.get_end()
            radius_line1 = DashedLine(ORIGIN, point_up, color=WHITE)
            radius_line2 = DashedLine(ORIGIN, point_down, color=WHITE)
            return VGroup(radius_line1, radius_line2)
            
        radius_lines = get_radius_lines(0)  # 初始位置的半径虚线
        
        # 动态更新动画
        t_values = [1, 0.5, 0, -0.5, -1, 1]  # E点移动的位置序列
        for t_target in t_values:
            new_parts = update_points(t_target)
            new_radius_lines = get_radius_lines(t_target)
            self.play(
                Transform(moving_parts, new_parts),
                Transform(radius_lines, new_radius_lines),
                run_time=1.5  # 增加到1.5秒
            )
            self.wait(0.8)  # 每次变换后等待0.8秒

        # 添加关键步骤说明
        step1 = Text("1. 连接OA和OB", font="SimSun").scale(0.5).to_edge(LEFT)
        
        # 在步骤1后添加虚线动画
        self.play(Write(step1), run_time=1.5)
        self.play(Create(radius_lines), run_time=1.5)
        self.wait(1)
        
        step2 = Text("2. 由于AB⊥直径，∠AEB = 90°", font="SimSun").scale(0.5).next_to(step1, DOWN, aligned_edge=LEFT)
        step3 = Text("3. OE是半径，OA = OB = R（半径）", font="SimSun").scale(0.5).next_to(step2, DOWN, aligned_edge=LEFT)
        step4 = Text("4. ∠OAE = ∠OBE（直角三角形性质）", font="SimSun").scale(0.5).next_to(step3, DOWN, aligned_edge=LEFT)

        steps = VGroup(step1, step2, step3, step4)

        # 在E点移动过程中显示步骤说明
        self.play(Write(step2), run_time=1.5)
        self.wait(1)
        self.play(Write(step3), run_time=1.5)
        self.wait(1)
        self.play(Write(step4), run_time=1.5)
        self.wait(1.5)

        # 添加结论说明
        conclusion = VGroup(
            Text("结论：", font="SimSun", color=YELLOW),
            Text("1. AE = BE（三角形全等）", font="SimSun"),
            Text("2. E点是弦AB的中点", font="SimSun")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.5).to_edge(RIGHT)

        self.play(Write(conclusion), run_time=2)
        self.wait(1.5)

        # 最终定理陈述 (调整到右侧)
        final_theorem = (VGroup(
            Text("垂径定理：", font="SimSun", color=YELLOW),
            Text("圆中垂直于直径的弦", font="SimSun"),
            Text("被直径平分", font="SimSun"),
            Text("弦的中点到圆心距离为：", font="SimSun"),
            Text("√(R²-(AB/2)²)", font="SimSun", color=BLUE),  # 改用Text替代MathTex
            Text("R: 半径  AB: 弦长", font="SimSun", color=GRAY)
        )
        .arrange(DOWN, aligned_edge=LEFT, buff=0.2)  # 减小行间距
        .scale(0.5)  # 稍微缩小文字
        .to_edge(RIGHT)  # 移到右边
        .shift(UP * 0.5))  # 向上移动一些

        self.play(
            FadeOut(steps),
            FadeOut(conclusion),
            FadeOut(radius_lines),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(Write(final_theorem), run_time=2)
        self.wait(2)


# manim -pqh circle_theorems.py PerpendicularDiameterTheorem