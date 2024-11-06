from repositories.dna_repository import DNARepository

class MutantService:
    def __init__(self):
        self.repository = DNARepository()

    def check_dna(self, dna):
        is_mutant = self.is_mutant(dna)
        self.repository.save_dna_result(dna, is_mutant)
        return is_mutant
    
    def is_mutant(self, dna):
        n = len(dna) 
        sequence_count = 0 

    
        def check_sequence(x, y, dx, dy): 
            letter = dna[x][y]
            for i in range(1, 4): 
                nx, ny = x + dx * i, y + dy * i 
                if nx < 0 or ny < 0 or nx >= n or ny >= n or dna[nx][ny] != letter:
                    return False
            return True

        for i in range(n):
            for j in range(n):
                if dna[i][j] != 'A' and dna[i][j] != 'T' and dna[i][j] != 'C' and dna[i][j] != 'G':
                    continue  
                if (j <= n - 4 and check_sequence(i, j, 0, 1)) or \
                (i <= n - 4 and check_sequence(i, j, 1, 0)) or \
                (i <= n - 4 and j <= n - 4 and check_sequence(i, j, 1, 1)) or \
                (i >= 3 and j <= n - 4 and check_sequence(i, j, -1, 1)):
                    sequence_count += 1
                    if sequence_count > 1:
                        return True  
        return False  
    
    def get_stats(self):
        return self.repository.get_stats()
