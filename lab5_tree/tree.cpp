// Практическая работа 5. Выполнили Князев Артём, Хапков Михаил, Позоян Рафаэль

#include <iostream>
#include <vector>


class BinTree {
private:
	// структура, представляющая вершину дерева
	struct TreeNode {
		int value = 0;
		//левый потомок
		TreeNode* lhs = nullptr;
		//правый потомок
		TreeNode* rhs = nullptr;
	};

	// корень дерева
	TreeNode* root_ = nullptr;

	// вставка значения в поддерево
	void NodeInsert(TreeNode*& cur, int num) {
		if (cur == nullptr) {
			cur = new TreeNode;
			cur->value = num;
		}
		else {
			if (cur->value < num)
				NodeInsert(cur->rhs, num);
			else
				NodeInsert(cur->lhs, num);
		}
	}
	// получение минимума из поддерева
	int NodeMin(TreeNode* cur) {
		if (cur->lhs == nullptr)
			return cur->value;
		else
			return NodeMin(cur->lhs);
	}
	// вывод поддерева
	void NodePrint(TreeNode* cur) {
		if (cur == nullptr)
			return;
		NodePrint(cur->lhs);
		std::cout << cur->value << " ";
		NodePrint(cur->rhs);
	}
	// удаление поддерева
	void NodeDestroy(TreeNode* cur) {
		if (cur == nullptr)
			return;
		NodeDestroy(cur->lhs);
		NodeDestroy(cur->rhs);
		delete cur;
	}

public:
	BinTree() = default;
	~BinTree() {
		NodeDestroy(root_);
	}
	// вставка значения в дереве
	void Insert(int num) {
		NodeInsert(root_, num);
	}
	// получение минимума из дерева
	int FindMin() {
		return NodeMin(root_);
	}
	// вывод дерева по возрастанию
	void PrintTree() {
		NodePrint(root_);
	}
};


int main() {

	BinTree tr;

	int opt = -1;

	while (opt != 4) {
		std::cout << "\nVvedite nomer:\n";
		std::cout << "1: Dobavit element\n";
		std::cout << "2: Vivesti minimum\n";
		std::cout << "3: Vivesti derevo\n";
		std::cout << "4: Vyhod\n";

		std::cout << "Vash vybor: ";
		std::cin >> opt;

		if (1 == opt) {
			std::cout << "Vvedite znachenie: ";
			int num = 0;
			std::cin >> num;
			tr.Insert(num);
		}
		else if (2 == opt) {
			std::cout << "Min znachenie: " << tr.FindMin() << "\n";
		}
		else if (3 == opt) {
			std::cout << "Derevo: ";
			tr.PrintTree();
			std::cout << std::endl;
		}
	}

	return 0;

}
