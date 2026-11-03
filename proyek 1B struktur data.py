class Node:
    def __init__(self, id_pegawai, nama, jabatan):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
        self.children = []  
        self.parent = None   

    def add_child(self, child_node):
        child_node.parent = self
        self.children.append(child_node)

    def __repr__(self):
        return f"[{self.id_pegawai}] {self.jabatan} - {self.nama}"


class OrganizationalTree:
    def __init__(self, root_node):
        self.root = root_node

    
    def insert_node(self, parent_id, id_pegawai, nama, jabatan):
        """Menambahkan pegawai baru di bawah atasan (parent_id) tertentu"""
        parent_node = self.search_node(self.root, parent_id)
        if parent_node:
            new_node = Node(id_pegawai, nama, jabatan)
            parent_node.add_child(new_node)
            print(f"[SUKSES] {jabatan} ({nama}) berhasil ditambahkan di bawah {parent_node.jabatan}.")
            return new_node
        else:
            print(f"[GAGAL] Parent dengan ID/Key '{parent_id}' tidak ditemukan!")
            return None

    
    def search_node(self, current_node, keyword):
        if current_node is None:
            return None

        if (keyword.lower() in current_node.id_pegawai.lower() or 
            keyword.lower() in current_node.nama.lower() or 
            keyword.lower() in current_node.jabatan.lower()):
            return current_node

        for child in current_node.children:
            found = self.search_node(child, keyword)
            if found:
                return found

        return None

   
    def preorder_traversal(self, node=None, visited=None):
        if visited is None:
            visited = []
        if node is None:
            node = self.root

        visited.append(node)

        for child in node.children:
            self.preorder_traversal(child, visited)

        return visited

   
    def inorder_traversal(self, node=None, visited=None):
        if visited is None:
            visited = []
        if node is None:
            node = self.root

        if not node.children:
            visited.append(node)
        else:
            self.inorder_traversal(node.children[0], visited)
            
            visited.append(node)
            
            for child in node.children[1:]:
                self.inorder_traversal(child, visited)

        return visited

    def postorder_traversal(self, node=None, visited=None):
        if visited is None:
            visited = []
        if node is None:
            node = self.root

        for child in node.children:
            self.postorder_traversal(child, visited)

        visited.append(node)

        return visited

   
    def display_tree(self, node=None, indent="", is_last=True):
        if node is None:
            node = self.root

        marker = "└── " if is_last else "├── "
        print(indent + marker + f"{node.jabatan} ({node.nama}) [{node.id_pegawai}]")

        indent += "    " if is_last else "│   "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            self.display_tree(child, indent, i == child_count - 1)



if __name__ == "__main__":
    print("=== INVENTARISASI STRUKTUR ORGANISASI UIN SUSKA RIAU ===\n")
    
    # 1. Inisialisasi Root (Rektor)
    rektor = Node("PEG-001", "Prof. Dr. Khairunnas Rajab, M.Ag.", "Rektor")
    org_tree = OrganizationalTree(rektor)

    # 2. Penyisipan Data Organisasi (insert_node)
    org_tree.insert_node("PEG-001", "PEG-002", "Drs. H. Promadi, Ph.D.", "Senat Universitas")
    org_tree.insert_node("PEG-001", "PEG-003", "Prof. Dr. H. Helmiati, M.Ag.", "Wakil Rektor I")
    org_tree.insert_node("PEG-001", "PEG-004", "Dr. H. Mas'ud Zein, M.Pd.", "Wakil Rektor II")
    org_tree.insert_node("PEG-001", "PEG-005", "Prof. Dr. Edi Erwan, S.Pt., M.Sc.", "Wakil Rektor III")
    org_tree.insert_node("PEG-001", "PEG-006", "Prof. Dr. Eng. Rika Ampuh Wijayanti", "Dekan Fakultas Sains dan Teknologi")

    # Penyisipan di bawah Dekan FST
    org_tree.insert_node("PEG-006", "PEG-007", "Dr. Monice, M.T.", "Wakil Dekan I")
    org_tree.insert_node("PEG-006", "PEG-008", "Dr. Harris Simaremare, M.T.", "Wakil Dekan II")
    org_tree.insert_node("PEG-006", "PEG-009", "Dr. Subaihan, M.Ag.", "Wakil Dekan III")
    org_tree.insert_node("PEG-006", "PEG-010", "Dr. Reski Mai Candra, S.T., M.Sc.", "Ketua Program Studi Teknik Informatika")

    # Penyisipan di bawah Kaprodi TIF
    org_tree.insert_node("PEG-010", "PEG-011", "M. Syafwan Al Hamdi, M.Kom.", "Sekretaris Program Studi")
    org_tree.insert_node("PEG-010", "PEG-012", "Fahmi Syahputra, M.Kom.", "Kepala Laboratorium Komputer")

    print("\n" + "="*60)
    print("STRUKTUR TREE ORGANISASI:")
    print("="*60)
    org_tree.display_tree()

    # 3. Pengujian Pencarian Data (search_node)
    print("\n" + "="*60)
    print("PENGUJIAN PENCARIAN (search_node):")
    print("="*60)
    query = "Teknik Informatika"
    hasil_cari = org_tree.search_node(org_tree.root, query)
    if hasil_cari:
        print(f"Hasil pencarian '{query}': DITEMUKAN!")
        print(f" Detail: {hasil_cari}")
        print(f" Atasan Langsung: {hasil_cari.parent.jabatan if hasil_cari.parent else 'Tidak ada (Root)'}")
    else:
        print(f"Hasil pencarian '{query}': TIDAK DITEMUKAN!")

    # 4. Pengujian Algoritma Traversal
    print("\n" + "="*60)
    print("PENGUJIAN ALGORITMA TRAVERSAL:")
    print("="*60)

    print("\n1. PREORDER TRAVERSAL (Root -> Children):")
    preorder_list = org_tree.preorder_traversal()
    for idx, n in enumerate(preorder_list, 1):
        print(f"  {idx}. {n.jabatan} ({n.nama})")

    print("\n2. INORDER TRAVERSAL (First Child -> Root -> Next Sibling):")
    inorder_list = org_tree.inorder_traversal()
    for idx, n in enumerate(inorder_list, 1):
        print(f"  {idx}. {n.jabatan} ({n.nama})")

    print("\n3. POSTORDER TRAVERSAL (Children -> Root):")
    postorder_list = org_tree.postorder_traversal()
    for idx, n in enumerate(postorder_list, 1):
        print(f"  {idx}. {n.jabatan} ({n.nama})")
