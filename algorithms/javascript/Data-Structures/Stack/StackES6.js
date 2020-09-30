/* Stack data-structure. It's work is based on the LIFO method (last-IN-first-OUT).
 * It means that elements added to the stack are placed on the top and only the
 * last element (from the top) can be reached. After we get access to the last
 * element, he pops from the stack.
 * This is a class-based implementation of a Stack. It provides functions
 * 'push' - to add an element, 'pop' - to remove an element from the top.
 * Also it implements 'length', 'last' and 'isEmpty' properties and
 * static isStack method to check is an object the instance of Stack class.
 */

// Class declaration
//

class Stack{

    constructor(){
        this.stack = []
        this.top = 0
    }

    // add a value to the end of the stack
    push(value){
        this.stack.push(value)
        this.top += 1
    }

    // returns and removes the last element of the stack
    pop(){
        if(this.stack !== 0){
            this.top -= 1
            return this.stack.pop()
        }
        throw new Error("Stack Underflow")
    }

    // returns the number of elements in the Stack
    get length(){
        return this.top
    }

    // retuns true if the stack is empty, false otherwise
    get isEmpty(){
        return this.top === 0
    }

    // returns the last element without removing it
    get last(){
        if(this.top !== 0){
            return this.stack[this.stack.length - 1]
        }
        return null
    }

    // check if an object is the instance of the stack class
    static isStack(el){
        return el instanceof Stack
    }
}

const newStack = new Stack()
console.log('Is it a Stack?,', Stack.isStack(newStack))
console.log('Is stack empty? ', newStack.isEmpty)
newStack.push('Hello world')
newStack.push(42)
newStack.push({ a: 6, b: 7 })
console.log('The length of stack is ', newStack.length)
console.log('Is stack empty? ', newStack.isEmpty)
console.log('Give me the last one ', newStack.last)
console.log('Pop the latest ', newStack.pop())
console.log('Pop the latest ', newStack.pop())
console.log('Pop the latest ', newStack.pop())
console.log('Is stack empty? ', newStack.isEmpty)
