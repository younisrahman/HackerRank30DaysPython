// create binary tree from array

// Node class
class Node {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }
}
const LEFT = 0;
const RIGHT = 1;

class TreeNode {
  constructor(value) {
    this.value = value;
    this.descendents = [];
    this.parent = null;
  }

  get left() {
    return this.descendents[LEFT];
  }

  set left(node) {
    this.descendents[LEFT] = node;
    if (node) {
      node.parent = this;
    }
  }

  get right() {
    return this.descendents[RIGHT];
  }

  set right(node) {
    this.descendents[RIGHT] = node;
    if (node) {
      node.parent = this;
    }
  }
}
class BinarySearchTree {
    constructor() {
      this.root = null;
      this.size = 0;
    }
    add(value) { /* ... */ }
    find(value) { /* ... */ }
    remove(value) { /* ... */ }
    getMax() { /* ... */ }
    getMin() { /* ... */ }
  }
  add(value) {
    const newNode = new BinaryTreeNode(value);
    if (this.root) {
      const { found, parent } = this.findNodeAndParent(value); // <1>
      if (found) { // duplicated: value already exist on the tree
        found.meta.multiplicity = (found.meta.multiplicity || 1) + 1; // <2>
      } else if (value < parent.value) {
        parent.setLeftAndUpdateParent(newNode);
      } else {
        parent.setRightAndUpdateParent(newNode);
      }
    } else {
      this.root = newNode;
    }

    this.size += 1;
    return newNode;
  }

  remove(value) {
    const nodeToRemove = this.find(value);
    if (!nodeToRemove) return false;

    // Combine left and right children into one subtree without nodeToRemove
    const nodeToRemoveChildren = this.combineLeftIntoRightSubtree(nodeToRemove);

    if (nodeToRemove.meta.multiplicity && nodeToRemove.meta.multiplicity > 1) {
      nodeToRemove.meta.multiplicity -= 1; // handle duplicated
    } else if (nodeToRemove === this.root) {
      // Replace (root) node to delete with the combined subtree.
      this.root = nodeToRemoveChildren;
      this.root.parent = null; // clearing up old parent
    } else {
      const side = nodeToRemove.isParentLeftChild ? 'left' : 'right';
      const { parent } = nodeToRemove; // get parent
      // Replace node to delete with the combined subtree.
      parent[side] = nodeToRemoveChildren;
    }

    this.size -= 1;
    return true;
  }
