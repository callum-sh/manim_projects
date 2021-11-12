from os import write
from manim import *
from numpy import matrix

class A1(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
        )


    def construct(self):
        matrix = [[-2, 2], [2, -3]]
        title = Tex(r"This is Question 3(i) from Tutorial 7")
        basel = MathTex(r"M = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}")
        VGroup(title, basel).arrange(DOWN)
        self.apply_matrix(matrix)

        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN)
        )

        transform_title = Tex("If we apply our matrix $M$ to a grid we get...")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        # grid = NumberPlane()
        # grid_title = Tex("Before the matrix is applied", font_size=40)
        # grid_title.move_to(transform_title)

        # self.add(grid, grid_title)
        # self.play(
        #     FadeOut(title),
        #     FadeIn(grid_title, shift=UP),
        #     Create(grid, run_time=3, lag_ratio=0.1)
        # )
        # self.wait()

        # M = np.array([
        #     [1, 2],
        #     [2, 1]
        # ])

        # e1_vec = Vector(np.array([1, 0]), color=GREEN)
        # e2_vec = Vector(np.array([0, 1]), color=RED)

        # e1_vec_new = Vector(M @ np.array([1, 0]), color=GREEN)
        # e2_vec_new = Vector(M @ np.array([0, 1]), color=RED)

        # matrix_anim = ApplyMatrix(M, grid)

        # grid_transform_title = Tex(r"That was $M$ applied to our grid.")
        # grid_transform_title.move_to(grid_title, UL)
        # self.play( 
        #     matrix_anim,
        #     Transform(e1_vec, e1_vec_new, rate_func=matrix_anim.get_rate_func(), run_time=matrix_anim.get_run_time()),
        #     Transform(e2_vec, e2_vec_new, rate_func=matrix_anim.get_rate_func(), run_time=matrix_anim.get_run_time()),
        #     FadeOut(grid, run_time=3)
        # )
        # self.wait()

class Vectors(VectorScene):
    def construct(self):

        plane = self.add_plane(animate=True).add_coordinates()
        vector = self.add_vector([1, 1], color=GREEN)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector = vector)

        vector2 = self.add_vector([-1, 2])
        self.write_vector_coordinates(vector = vector2)

class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True
        )

    def construct(self):
        matrix = [[1, 2], [2, 1]]

        matrix_tex = MathTex(r"A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}").to_edge(UL)


        vec1 = self.add_vector([1, 1], color=YELLOW)
        self.vector_to_coords(vector = vec1)

        vec2 = self.add_vector([-1, 1], color=YELLOW)
        self.vector_to_coords(vector = vec2)

        self.add_transformable_mobject(vec1, vec2)
        self.add_background_mobject(matrix_tex)
        self.apply_matrix(matrix)

        self.wait()