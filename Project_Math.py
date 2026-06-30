# Código Limpo - Att. Eduardo

import matplotlib.pyplot as plt

class Menu:
    def __init__(self):
        self.dim = 0
        self.grafico = Grafico()
        self.vetor = Vetor([])

    def mostrar_titulo(self, titulo):
        print("\n====================")
        print(f"{titulo:^20}")
        print("====================")

    def visualizar_grafico(self, vetores):
        self.mostrar_titulo("Ver espaço na interface?")
        print("1 - Sim")
        print("2 - Não")
        op = int(input("Escolha: "))

        if op == 1:
            if self.dim == 2:
                self.grafico.exibir_R2(*vetores)

            elif self.dim == 3:
                self.grafico.exibir_R3(*vetores)

        elif op == 2:
            pass

        else:
            print("Opção Inválida!")

    def executar(self):
        while True:
            self.mostrar_titulo("MENU PRINCIPAL")
            print("1 - Vetores R²")
            print("2 - Vetores R³")
            print("0 - Sair")

            opcao = int(input("Escolha: "))

            if opcao == 0:
                print("Encerrando...")
                break

            if opcao == 1:
                self.dim = 2
                self.sub_menu()

            elif opcao == 2:
                self.dim = 3
                self.sub_menu()

            else:
                print("Opção inválida!")
                continue

    def sub_menu(self):
        self.mostrar_titulo("OPERAÇÕES")
        print("\nEscolha uma operação vetorial")
        print("1 - Multiplicação por escalar")
        print("2 - Soma de vetores")
        print("3 - Combinação linear")
        print("4 - Dependência linear")

        operacao = input("Escolha: ")

        # Multiplicação por escalar
        if operacao == '1':
            resultado = self.vetor.executar_multiplicacao(self.dim)
            self.visualizar_grafico(resultado)

        # Soma
        elif operacao == '2':
            vetores = self.vetor.executar_soma(self.dim)
            self.visualizar_grafico(vetores)

        # Combinação Linear
        elif operacao == '3':
            resultado = self.vetor.executar_combinacao(self.dim)
            self.visualizar_grafico(resultado)

        elif operacao == '4':
            self.vetor.verificar_dependencia(self.dim)

        else:
            print("Opção Inválida!")

class Vetor:
    def __init__(self, componentes):
        self.componentes = componentes

    def multiplicar_escalar(self, escalar):
        resultado = []

        for valor in self.componentes:
            resultado.append(valor * escalar)

        return Vetor(resultado)

    def somar(self, outro):
        resultado = []

        for i in range(len(self.componentes)):
            resultado.append(
                self.componentes[i] + outro.componentes[i]
            )

        return Vetor(resultado)

    def combinacao_linear(self, a, outro, b):
        v1 = self.multiplicar_escalar(a)
        v2 = outro.multiplicar_escalar(b)

        return v1.somar(v2)

    def __str__(self):
        return str(tuple(self.componentes))

    def executar_multiplicacao(self, dimensao):
        print("\nDigite o vetor:")
        vetor = self.criar_vetor(dimensao)

        escalar = float(input("Digite o escalar: "))

        resultado = vetor.multiplicar_escalar(escalar)

        print(f"Resultado: {resultado}")

        return (vetor, resultado)

    def executar_soma(self, dimensao):
        print("\nPrimeiro vetor:")
        v1 = self.criar_vetor(dimensao)

        print("\nSegundo vetor:")
        v2 = self.criar_vetor(dimensao)

        resultado = v1.somar(v2)
        print(f"Resultado: {resultado}")
        return v1, v2, resultado

    def executar_combinacao(self, dimensao):
        print("\nPrimeiro vetor:")
        v1 = self.criar_vetor(dimensao)

        print("\nSegundo vetor:")
        v2 = self.criar_vetor(dimensao)

        a = float(input("\nDigite o escalar a: "))
        b = float(input("Digite o escalar b: "))

        av1 = v1.multiplicar_escalar(a)
        bv2 = v2.multiplicar_escalar(b)

        resultado = av1.somar(bv2)

        print(f"\n{a:g}({v1}) + {b:g}({v2})")
        print(f"= {av1} + {bv2}")
        print(f"= {resultado}")

        print("\nResumo:")
        print(f"Resultado final: {resultado}")
        print("Vetor gerado por combinação linear de v1 e v2")

        return (v1, v2, resultado)

    def criar_vetor(self, dimensao):
        componentes = []

        print()

        for i in range(dimensao):
            valor = float(input(f"Digite a componente {i+1}: "))
            componentes.append(valor)

        return Vetor(componentes)

    def verificar_dependencia(self, dimensao):        # Dependencia

        print("\nPrimeiro vetor:")
        v1 = self.criar_vetor(dimensao)

        print("\nSegundo vetor:")
        v2 = self.criar_vetor(dimensao)

        if dimensao == 2:

            determinante = (
                    v1.componentes[0] * v2.componentes[1]
                    - v1.componentes[1] * v2.componentes[0]
            )
            print(f"det = {determinante:g}")

            if determinante == 0:
                print("\nOs vetores estão na mesma direção (colineares)")
                print("Os vetores são linearmente dependentes.")
                print("Não formam uma base de R²")
            else:
                print("\nOs vetores são linearmente independentes.")
                print("Formam uma base de R² (geram todo o plano)")

        elif dimensao == 3:

            print("\nTerceiro vetor:")
            v3 = self.criar_vetor(dimensao)

            a = v1.componentes
            b = v2.componentes
            c = v3.componentes

            determinante = (
                    a[0] * (b[1] * c[2] - b[2] * c[1])
                    - a[1] * (b[0] * c[2] - b[2] * c[0])
                    + a[2] * (b[0] * c[1] - b[1] * c[0])
            )
            print(f"det = {determinante:g}")

            if determinante == 0:
                print("\nOs vetores estão no mesmo plano (coplanares)")
                print("Os vetores são linearmente dependentes.")
                print("Não formam uma base de R³")
            else:
                print("\nOs vetores são linearmente independentes.")
                print("Formam uma base de R³ (geram todo o espaço tridimensional)")

class Grafico:
    def __init__(self):
        pass

    def exibir_R2(self, *vetores):

        plt.figure()

        cores = ["blue", "green", "red"]
        nomes = ["V1", "V2", "Resultado"]

        plt.axvline(0, color='black', linewidth=1)
        plt.axhline(0, color='black', linewidth=1)
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.gca().set_aspect('equal', adjustable='box')

        for i, vetor in enumerate(vetores):
            x = vetor.componentes[0]
            y = vetor.componentes[1]

            plt.quiver(
                0, 0,
                x, y,
                color=cores[i],
                angles='xy',
                scale_units='xy',
                scale=1,
                label=nomes[i]
            )

            plt.scatter(x, y, color=cores[i])
            plt.text(x, y, nomes[i])

        xs = [v.componentes[0] for v in vetores]
        ys = [v.componentes[1] for v in vetores]

        lim_x = max(abs(x) for x in xs) + 1
        lim_y = max(abs(y) for y in ys) + 1

        plt.xlim(-lim_x, lim_x)
        plt.ylim(-lim_y, lim_y)

        plt.title("Espaço R2")

        plt.xlabel("Eixo X")
        plt.ylabel("Eixo Y")

        plt.legend(loc="upper left", bbox_to_anchor=(-0.65, 1))

        plt.subplots_adjust(
        left=0.20,
        right=0.75,
        bottom=0.15,
        top=0.90
        )

        plt.scatter(0, 0, color="black", s=40, zorder=5)

        plt.show()

    def exibir_R3(self, *vetores):

        xs = []
        ys = []
        zs = []

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        cores = ["blue", "green", "red"]
        nomes = ["V1", "V2", "Resultado"]

        for i, vetor in enumerate(vetores):
            x = vetor.componentes[0]
            y = vetor.componentes[1]
            z = vetor.componentes[2]

            ax.quiver(
            0, 0, 0,
            x, y, z,
            color=cores[i],
            arrow_length_ratio=0.1,
            label=nomes[i]
            ) 

            ax.scatter(x, y, z, color=cores[i])
            ax.text(x, y, z, nomes[i], fontsize=10)

            xs.append(x)
            ys.append(y)
            zs.append(z)

        limite = max(
            max(abs(v) for v in xs),
            max(abs(v) for v in ys),
            max(abs(v) for v in zs)
        ) + 1

        ax.set_xlim([-limite, limite])
        ax.set_ylim([-limite, limite])
        ax.set_zlim([-limite, limite])

        ax.set_xlabel("Eixo X")
        ax.set_ylabel("Eixo Y")
        ax.set_zlabel("Eixo Z")

        ax.set_title("Espaço R³")

        ax.scatter(0, 0, 0, color="black")

        ax.grid(True)
        ax.view_init(elev=20, azim=30)
        ax.set_box_aspect([1, 1, 1])

        ax.legend(loc="upper left", bbox_to_anchor=(-0.3, 1))
        plt.subplots_adjust(
        left=0.20,
        right=0.80,
        bottom=0.10,
        top=0.90
        )
        plt.show()

menu = Menu()
menu.executar()