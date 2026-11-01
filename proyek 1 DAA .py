class SearchResult:
    def __init__(self, pattern, latin_name="-", dino_id="-", index="-", score_percentage=0.0, matched_chars=0, pattern_length=0, status="Not Found"):
        self.pattern = pattern
        self.latin_name = latin_name
        self.dino_id = dino_id
        self.index = index
        self.score_percentage = score_percentage
        self.matched_chars = matched_chars
        self.pattern_length = pattern_length
        self.status = status

    def is_better_than(self, other):
        """
        Kriteria pengurutan:
        1. Skor kemiripan tertinggi (Descending)
        2. Indeks posisi kemunculan terkecil (Ascending)
        """
        if self.score_percentage != other.score_percentage:
            return self.score_percentage > other.score_percentage
        if isinstance(self.index, int) and isinstance(other.index, int):
            return self.index < other.index
        return True


class DNAPaleogenomicsMatcher:
    def __init__(self, dataset):
        self.dataset = dataset
        self.total_operations = 0

    def compute_lps(self, pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            self.total_operations += 1
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def kmp_search_single(self, text, pattern):
        n = len(text)
        m = len(pattern)
        
        lps = self.compute_lps(pattern)
        i = 0  # Indeks untuk text
        j = 0  # Indeks untuk pattern
        
        while i < n:
            self.total_operations += 1
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                return (i - j, 100.0, m, "Exact Match")
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        lps_prefix = self.compute_lps(prefix_pattern)
        i = 0
        j = 0
        sub_m = m - 1
        
        while i < n:
            self.total_operations += 1
            if prefix_pattern[j] == text[i]:
                i += 1
                j += 1

            if j == sub_m:
                match_pos = i - j
                if match_pos + m - 1 < n:
                    score = ((m - 1) / m) * 100.0
                    return (match_pos, score, m - 1, "End-Mutated")
                break
            elif i < n and prefix_pattern[j] != text[i]:
                if j != 0:
                    j = lps_prefix[j - 1]
                else:
                    i += 1

        return None

    def search_pattern(self, pattern):
        for dino_id, latin_name, length, dna_seq in self.dataset:
            res = self.kmp_search_single(dna_seq, pattern)
            if res is not None:
                idx, score, matched, status = res
                return SearchResult(pattern, latin_name, dino_id, idx, score, matched, len(pattern), status)
        return SearchResult(pattern, "-", "-", "-", 0.0, 0, len(pattern), "Not Found")

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            self.total_operations += 1
            if left[i].is_better_than(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    def execute_pipeline(self, patterns):
        self.total_operations = 0
        raw_results = []
        for pat in patterns:
            raw_results.append(self.search_pattern(pat))
        
        sorted_results = self.merge_sort(raw_results)
        return sorted_results, self.total_operations


# ==============================================================================
# SIMULASI DAN PENGUJIAN KHUSUS DINO NOMOR 9: Diplodocus carnegii
# ==============================================================================

# Data Sekuens DNA Nomor 9 dari Dataset
dataset_dino_9 = [
    (
        9, 
        "Diplodocus carnegii", 
        256, 
        "CTATTATCAGATGTCGCCGCATCTTCCGAACTGCACCTCGGCTTGCATAGCTGGAATTGTCTAGAGCGGGCCAGAGCTATGTTAAAAGTCCCCGTAGTGTTACGAAACCTGTAGAATTCAATTGATCTGTGCAAATCTCTATGGTACTCTTCTACTCCTCGGAGTGAAGGGCAACCCAACGCACAGCCCCATTTGACACCACCCACAGGAACTCGTCCTTTACTACTTCGCGACTCAGGGGGTCGCCGTTCCGAGG"
    )
]

test_patterns = [
    "TTTTTTTTTTTTTTTT",  
    "CTATTATCAGATGTCG",  
    "CTATTATCAGATGTCA"   
]


matcher = DNAPaleogenomicsMatcher(dataset_dino_9)
results, total_ops = matcher.execute_pipeline(test_patterns)


print("=== HASIL PEMETAAN FRAGMEN DNA (TERURUT SKOR TERTINGGI) ===")
for idx, res in enumerate(results, 1):
    print(f"{idx}. Pola: \"{res.pattern}\"")
    print(f"   Nama Latin: {res.latin_name}")
    print(f"   Nomor: {res.dino_id}")
    print(f"   Indeks: {res.index}")
    if res.score_percentage > 0:
        print(f"   Skor Kemiripan: {res.score_percentage:.1f}% ({res.matched_chars}/{res.pattern_length})")
    else:
        print(f"   Skor Kemiripan: 0% (0/{res.pattern_length})")
    print(f"   Status: {res.status}")

print("\nMetrik Eksekusi:")
print(f"- Total Operasi Dasar (Perbandingan Karakter): {total_ops} operasi")
