from manim import *
import numpy as np

class Intro(Scene):    
    def construct(self):
        Vertices1 = [1,2,3,4,5]
        Edges1 = [(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)]
        graph = Graph(Vertices1, Edges1, layout_scale=3,layout="circular",labels=True, vertex_config={i: {"fill_color":GREEN} for i in range(1,6)})
        path = "./fig2.png"
        path2 = "./IIITLogo.png"

        img = ImageMobject(path)
        im2 = ImageMobject(path2)

        im2.height = 1.2
        im2.shift(5.5*LEFT + 3*UP)
        img.height = 8
        
        self.add(img,im2)
        t = Text("5-MICC, ICASSP 2022")
        t.scale(0.75)
        t.shift(1.25*UP)
        y = Text("Investigating the influence of super spreaders on driving",weight = SEMIBOLD, color = YELLOW)
        y2 = Text("COVID-19 pandemic in India using GSP",weight = SEMIBOLD, color = YELLOW)
        y2.next_to(y,0.5*DOWN)
        y = VGroup(y,y2)
        y.scale(0.6)
        y.shift(0.25*UP)

        People1 = Text("Supervisor: Dr Santosh Nannuru",weight = SEMIBOLD)
        People2 = Text("Tutor: Darapu Sudeepini",weight = SEMIBOLD)
        People3 = Text("Undergraduates: Ashuthosh Bharadwaj, Sasanka GRS, Loay Rashid",weight = SEMIBOLD)
        People1.scale(0.35).shift(1.5*DOWN)
        People2.scale(0.35).shift(1.85*DOWN)
        People3.scale(0.35).shift(2.20*DOWN)

        J = VGroup(People1,People2, People3)

        #  animation starts

        self.play(Write(t,run_time = 1))
        self.play(FadeIn(y, run_time = 1))
        self.add(People1, People2, People3, t, y)
        self.wait()
        self.play(FadeOut(y,J))
        self.remove(img,im2)

        self.play(Transform(t,graph,run_time=1))
        self.play(Rotate(t,4*PI))
        self.play(FadeOut(t,run_time = 0.5))    
        
        p1 =  "./i1.png"
        p2 =  "./j1.png"
        p3 =  "./k1.png"
        p4 =  "./l1.png"
        p5 =  "./m1.png"

        pers = "./human.png"
        comp = "./comp.png"

        pr1 = ImageMobject(p1)
        pr2 = ImageMobject(p2)        
        pr3 = ImageMobject(p3)
        pr4 = ImageMobject(p4)
        pr5 = ImageMobject(p5)
        hum = ImageMobject(pers)
        comp = ImageMobject(comp)

        pr1.scale(0.6)
        pr2.scale(0.6)
        pr3.scale(0.6)
        pr4.scale(0.6)
        pr5.scale(0.6)

        comp.scale(0.8)
        hum.scale(0.4)

        vertices = [1,2,3,4,5]
        edges = [(1,2), (1,3), (2,3), (3,5), (5,1), (5,4), (4,2), (5,2),(4,3)]
        spl = {i:{"stroke_color": GREEN} for i in edges}

        humlist = [hum.copy() for i in range(1,6)]
        complist = [comp.copy() for i in range(1,6)]

        spl1 = {i:humlist[i-1] for i in range(1,6)}
        spl2 = {i:complist[i-1] for i in range(1,6)}
        

        g1 = Graph(vertices, edges,layout_scale=2, layout='spring', vertex_mobjects={1:pr1 , 2:pr2, 3:pr3, 4:pr4, 5:pr5}, edge_config={(5,1): {"stroke_color": RED}, (5,2): {"stroke_color": GREEN},(4, 3): {"stroke_color": RED}, (1,3): {"stroke_color": GREEN}})
        Soc = Graph(vertices, edges,layout_scale=2, layout= 'circular', vertex_mobjects = spl1 , edge_config=spl)
        Serv = Graph(vertices, edges,layout_scale=2, layout= 'kamada_kawai', vertex_mobjects=spl2)
        

        tit1 = Tex("Protein Dynamics").shift(3*UP)
        tit2 = Tex("Social Networks").shift(3*UP)
        tit3 = Tex("Server Communication Networks").shift(3*UP)


        self.add(g1)
        self.wait(0.5)
        self.play(Write(tit1,run_time = 0.75))
        self.play(FadeOut(tit1,run_time = 0.75))
        self.remove(g1)

        
        self.add(Soc)
        self.wait(0.5)                
        self.play(Write(tit2,run_time = 0.75))
        self.play(FadeOut(tit2,run_time = 0.75))
        self.remove(Soc)

        
        self.add(Serv)
        self.wait(0.5)
        self.play(Write(tit3,run_time = 0.75))
        self.play(FadeOut(tit3,run_time = 0.75))
        self.remove(Serv)
        
        nod = lambda x : VGroup(Sphere(radius=0.2).set_fill(RED, opacity=1) , Tex(str(x)))
        
        CEns = {i: nod(i)  for i in range(1,6)}
        x = Graph(Vertices1, Edges1, layout="circular",labels=False,vertex_mobjects=CEns)
        return x, CEns

class ThreeDCameraRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.play(Create(axes))
        self.move_camera(phi=75*DEGREES, theta=30*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(0.5)
        self.stop_ambient_camera_rotation()

          
class THEONE(ThreeDScene):
    def construct(self):
        t,Themnodes = Intro.construct(self)
        t.scale(0.5)
        t.shift(3*UP + 3*RIGHT)
        self.add(t)
        ThreeDCameraRotation.construct(self)
        Centers = [((list(Themnodes.values()))[i-1]).get_center() for i in range(1,6)]
        
        s0 = np.random.randint(low = -2,high= 3,size = (5,))
        last = np.random.randint(low = -2,high= 3,size = (5,))
        last[np.where(last == s0)] = np.random.choice([-1.5,2.75,0.5,-0.2]) 
    
        Signal = [(Line(Centers[i], Centers[i] + np.array([0,0,s0[i]]),color = YELLOW)) for i in range(5)]
        Signals = VGroup(*Signal)
        
        self.add(Signals)

        new = [ValueTracker(s0[i]) for i in range(5)] 

        for i in range(5):       
            Signal[i].add_updater(lambda x: x.become(Line(Centers[i],Centers[i] + np.array([0,0, (new[i].get_value())]), color = YELLOW)))
            self.play(ApplyMethod(new[i].set_value,last[i])) 
            self.add((Line(Centers[i],Centers[i] + np.array([0,0,last[i]]),color = YELLOW)))
    
        # self.play([ApplyMethod(new[i].set_value,last[i]) for i in range(5)])
        # whatineed = [ for i in range(5)]
        # self.play(*whatineed)
        self.wait(1)


class Checker(Scene):
    def construct(self):
        path = "./fig2.png"
        path2 = "./IIITLogo.png"

        img = ImageMobject(path)
        im2 = ImageMobject(path2)

        im2.height = 1.2
        im2.shift(5.5*LEFT + 3*UP)
        img.height = 8
        
        self.add(img,im2)
        t = Text("5-MICC, ICASSP 2022")
        t.shift(1.25*UP)
        y = Text("Investigating the influence of super spreaders on driving COVID pandemic in India")
        y.scale(0.5)
        y.shift(0.25*UP)

        People1 = Text("Supervisor: Dr Santosh Nannuru", )
        People2 = Text("Tutor: Darapu Sudeepini",)
        People3 = Text("Undergraduates: Ashuthosh Bharadwaj, Sasanka GRS, Loay Rashid",)
        People1.scale(0.45).shift(1.5*DOWN)
        People2.scale(0.45).shift(1.85*DOWN)
        People3.scale(0.45).shift(2.20*DOWN)
        self.add(People1, People2, People3, t, y)

class checker2(Scene):
    def construct(self):
        path = "./fig2.png"
        path2 = "./IIITLogo.png"

        img = ImageMobject(path)
        im2 = ImageMobject(path2)

        im2.height = 1.2
        im2.shift(5.5*LEFT + 3*UP)
        img.height = 8
        
        self.add(img,im2)
        t = Text("5-MICC, ICASSP 2022")
        t.scale(0.75)
        t.shift(1.25*UP)
        y = Text("Investigating the influence of super spreaders on driving",weight = SEMIBOLD, color = YELLOW)
        y2 = Text("COVID-19 pandemic in India using GSP",weight = SEMIBOLD, color = YELLOW)
        y2.next_to(y,0.5*DOWN)
        y = VGroup(y,y2)
        y.scale(0.6)
        y.shift(0.25*UP)

        People1 = Text("Supervisor: Dr Santosh Nannuru",weight = SEMIBOLD)
        People2 = Text("Tutor: Darapu Sudeepini",weight = SEMIBOLD)
        People3 = Text("Undergraduates: Ashuthosh Bharadwaj, Sasanka GRS, Loay Rashid",weight = SEMIBOLD)
        People1.scale(0.35).shift(1.5*DOWN)
        People2.scale(0.35).shift(1.85*DOWN)
        People3.scale(0.35).shift(2.20*DOWN)

        J = VGroup(People1,People2, People3)

        #  animation starts

        self.play(Write(t,run_time = 1))
        self.play(FadeIn(y, run_time = 1))
        self.add(People1, People2, People3, t, y)
        self.wait()
        self.play(FadeOut(y,J))
        self.remove(img,im2)


        

