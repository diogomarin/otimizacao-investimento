dormitorios = ['Sao Paulo', 'Flamengo', 'Coritiba', 'Cruzeiro', 'Fortaleza']

preferenciais = [('Amanda', ('Cruzeiro', 'Coritiba')),
                 ('Pedro', ('Sao Paulo', 'Fortaleza')),
                 ('Marcos', ('Flamengo', 'Sao Paulo')),
                 ('Priscila', ('Sao Paulo', 'Fortaleza')),
                 ('Jessica', ('Flamengo', 'Cruzeiro')),
                 ('Paulo', ('Coritiba', 'Fortaleza')),
                 ('Fred', ('Fortaleza', 'Flamengo')),
                 ('Suzana', ('Cruzeiro', 'Coritiba')),
                 ('Laura', ('Cruzeiro', 'Coritiba')),
                 ('Ricardo', ('Coritiba', 'Flamengo'))]

dominio = [(0, (len(dormitorios)*2) - i - 1) for i in range(0, len(dormitorios) * 2)]
