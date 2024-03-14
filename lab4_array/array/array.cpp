// Практическая работа #4: Позоян, Князев, Хапков

#include <iostream>
#include <vector>

// Комментирование действий
#define COMMENTS

// Смежное представление
class Array {
private:
	std::vector<int> array;
public:
	void addEl(int value) {
		array.push_back(value);
#ifdef COMMENTS
	std::cout << ">>> You have added an element: " << value << std::endl;
#endif
	}

	void delEl(int index) {
		if (array.size() > 0 and index >= 0) {
			array.erase(array.begin() + index);
		}
#ifdef COMMENTS
	std::cout << ">>> You have deleted an element: " << array[index] << std::endl;
#endif
	}

	void showSize() {
		std::cout << "Size of your array: " << array.size() << std::endl;
	}

	void show() {
		std::cout << "Your array: {";
		for (int i = 0; i < array.size(); i++) {
			if (i == array.size()-1) {
				std::cout << array[i];
			}
			else {
				std::cout << array[i] << " ";
			}
		}
		std::cout << "}" << std::endl;
	}
};


// Связное представление

class Element {
public:
	int data;
	Element* next_data;

	Element(int data) {
		this->data = data;
		next_data = nullptr;
	}
};

class ArrayMethods {
private:
	Element* head;
public:
	ArrayMethods() {
		head = nullptr;
	}

	void addEl(int data) {
#ifdef COMMENTS
		std::cout << ">>> You have added an element: " << data << std::endl;
#endif
		Element* newElement = new Element(data);

		if (head == nullptr) {
			head = newElement;
		}
		else {
			Element* temp = head;

			while (temp->next_data != nullptr) {
				temp = temp->next_data;
			}
			temp->next_data = newElement;
		}
	}

	void delEl(int data) {
#ifdef COMMENTS
		std::cout << ">>> You have deleted an element: " << data << std::endl;
#endif
		if (head == nullptr)
			return;

		if (head->data == data) {
			Element* temp = head;
			head = head->next_data;
			delete temp;
			return;
		}

		Element* temp = head;
		while (temp->next_data != nullptr && temp->next_data->data != data) {
			temp = temp->next_data;
		}

		if (temp->next_data != nullptr) {
			Element* elementToDelete = temp->next_data;
			temp->next_data = temp->next_data->next_data;
			delete elementToDelete;
		}
	}

	void printList() {
		Element* temp = head;
		std::cout << "Your array: { ";
		while (temp != nullptr) {
			std::cout << temp->data << " ";
			temp = temp->next_data;
		}
		std::cout << "}" << std::endl;
	}

	void showSize() {
		int count = 0;
		Element* temp = head;
		while (temp != nullptr) {
			count++;
			temp = temp->next_data;
		}
		std::cout << "Size of your array: " << count << std::endl;
	}
};




int main() {
	Array array;
	array.addEl(15);
	array.addEl(111);
	array.addEl(3);

	array.show();
	array.showSize();

	array.addEl(34);

	array.show();
	array.showSize();

	array.delEl(2);

	array.show();
	array.showSize();

	std::cout << "----------------------------------" << std::endl;
	std::cout << "----------------------------------" << std::endl;
	std::cout << "----------------------------------" << std::endl;

	ArrayMethods arr;
	arr.addEl(99);
	arr.addEl(66);
	arr.addEl(33);

	arr.printList();
	arr.showSize();

	arr.delEl(99);

	arr.printList();
	arr.showSize();
}