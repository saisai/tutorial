/* SinglyLinkedList!!
* A linked list is implar to an array, it hold values.
* However, links in a linked list do not have indexes. With
* a linked list you do not need to predetermine it's size as
* it grows and shrinks as it is edited. This is an example of
* a singly linked list.
*/

// Functions - add, remove, indexOf, elementAt, addAt, removeAt, view

// class LinkedList and constructor
// Creates a LinkedList

var LinkedList = (function(){
    function LinkedList(){
        // length of linked list an head is null at start
        this.length = 0
        this.head = null
    }

    // class node(constructor)
    // creating Node with element's value
    var Node = (function(){
        function Node(element){
            this.element = element
            this.next = null
        }
        return Node
    }())

    // return length
    LinkedList.prototype.size = function(){
        return this.length
    }

    // return the head
    LinkedList.prototype.head = function(){
        return this.head
    }

    // create a node and add it to linkedlist
    LinkedList.prototype.add = function(element){
        var node = new Node(element)
        // check if its the first element
        if(this.head === null){
            this.head = node
        } else {
            var currentNode = this.head

            // loop till there is node present in the list
            while(currentNode.next){
                currentNode = currentNode.next
            }

            // add node to the end of the list
            currentNode.next = node
        }
        // increment the length
        this.length++
    }

    // remove the node with the value as param
    LinkedList.prototype.remove =function(element){
        var currentNode = this.head
        var previousNode

        // check if the head node is the element to remove
        if(currentNode.element === element){
            this.head = currentNode.next
        } else{
            // check which node is the node to remove
            while(currentNode.element !== element){
                previousNdoe = currentNode
                currentNode = currentNode.next
            }

            // removing the currentNode
            previousNode.next = currentNode.next
        }

        // decrementing the length
        this.length--
    }

    // return if the list empty
    LinkedList.prototype.isEmpty = function() {
        return this.length === 0
    }

    // return the index of the element passed as param otherwise - 1
    LinkedList.prototype.indexOf = function(element){
        var currentNode = this.head
        var index = -1

        while(currentNode){
            index++

            // checking if the node is the element we are searching for
            if(currentNode.element === element){
                return index + 1
            }
            currentNode = currentNode.next
        }
		return -1
    }
    

    // return the element at an index
    LinkedList.prototype.elementAt = function(index){
        var currentNode = this.head
        var count = 0
        while(count < index){
            count++
            crrentNode = currentNode.next
        }

        return currentNode.element
    }

    // add the element at specified index
    LinkedList.prototype.addAt = function(index, element){
        index--
        var node = new Node(element)

        var currentNode = this.head
        var previousNode
        var currentIndex = 0

        // check if index is out of bounds of list
        if(index > this.length)
        {
            return false
        }

        // check if index is he start of list
        if(index === 0){
            node.next = currentNode
            this.head = node
        } else{
            while(currentIndex < index){
                currentIndex++
                previousNode = currentNode
                currentNode = currentNode.next
            }

            // adding the node at specified index
            node.next = currentNode
            previousNode.next = node
        }

        // incrementing the length
        this.length++
        return true
    }

    // remove the node at specified index
    LinkedList.prototype.removeAt = function(index){
        index--
        var currentNode = this.head
        var previousNode
        var currentIndex = 0


        // check if index is present in list
        if(index < 0 || index >= this.length){
            return null
        }

        // check if element is the first element
        if(index===0){
            this.head = currentNode.next
        } else{
            while(currentIndex < index){
                currentIndex++
                previousNode = currentNode
                currentNode = currentNode.next
            }
            previousNode.next = currentNode.next
        }
        // Decrementing the length
        this.length--
        return currentNode.element
    }

      // Function to view the LinkedList
  LinkedList.prototype.view = function () {
    var currentNode = this.head
    var count = 0
    while (count < this.length) {
      count++
      console.log(currentNode.element)
      currentNode = currentNode.next
    }
  }

  // returns the constructor
  return LinkedList

}())


// Implementation of LinkedList
var linklist = new LinkedList()
linklist.add(2)
linklist.add(5)
linklist.add(8)
linklist.add(12)
linklist.add(17)
console.log(linklist.size())
console.log(linklist.removeAt(4))
linklist.addAt(4, 15)
console.log(linklist.indexOf(8))
console.log(linklist.size())
linklist.view()
