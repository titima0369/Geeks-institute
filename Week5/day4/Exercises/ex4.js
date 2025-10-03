// todo
export class TodoList {
  constructor() {
    this.tasks = [];
  }

  addTask(task) {
    this.tasks.push({ task, completed: false });
  }

  completeTask(task) {
    const item = this.tasks.find(t => t.task === task);
    if (item) item.completed = true;
  }

  listTasks() {
    return this.tasks;
  }
}
// app
import { TodoList } from "./todo.js";

const todo = new TodoList();

todo.addTask("Buy groceries");
todo.addTask("Finish project");
todo.addTask("Read a book");

todo.completeTask("Buy groceries");

console.log(todo.listTasks());
