from repositories.dna_repository import DNARepository # importa el repositorio para interactuar con la bd

class MutantService:
    def __init__(self):
        self.repository = DNARepository() # instancia la clase DNARepository para usar sus metodos

    def check_dna(self, dna): # verifica si una secuencia de adn es mutante
        is_mutant = self.is_mutant(dna)
        self.repository.save_dna_result(dna, is_mutant) # guarda el resultado en la bd
        return is_mutant 
    
    def is_mutant(self, dna): 
        n = len(dna) 
        sequence_count = 0 

    
        def check_sequence(x, y, dx, dy): # verifica si existe una secuencia de 4 caract iguales 
            letter = dna[x][y] # toma el primer caracter de la secuencia en la posicion (x, y)
            for i in range(1, 4):  # recorre los siguientes 3 caract en la direccion indicada por dx , dy 
                nx, ny = x + dx * i, y + dy * i 
                if nx < 0 or ny < 0 or nx >= n or ny >= n or dna[nx][ny] != letter:
                    return False
            return True

        for i in range(n): # recorre todas las posiciones del ADN y verifica si en esa posicion comeienza una secuencua de 4 caract consecutivos iguales en cualquier direccion
            for j in range(n):
                if dna[i][j] != 'A' and dna[i][j] != 'T' and dna[i][j] != 'C' and dna[i][j] != 'G': # verificacion de caract
                    continue  
                if (j <= n - 4 and check_sequence(i, j, 0, 1)) or \
                (i <= n - 4 and check_sequence(i, j, 1, 0)) or \
                (i <= n - 4 and j <= n - 4 and check_sequence(i, j, 1, 1)) or \
                (i >= 3 and j <= n - 4 and check_sequence(i, j, -1, 1)):
                    sequence_count += 1 # si hay una secuencia valida incrementa el contador
                    if sequence_count > 1: # si el contador es mayor a uno -> encontro un mutante
                        return True  
        return False  
    
    def get_stats(self):
        return self.repository.get_stats() #devuelve las estadísticas de los ADN almacenados, llamando al método get_stats del repositorio
