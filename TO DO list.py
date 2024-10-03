import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ To-Do List ✨")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # Load tasks
        self.tasks = self.load_tasks()

        # Header
        header_frame = tk.Frame(root, bg="#4CAF50", pady=20)
        header_frame.pack(fill=tk.X)
        header_label = tk.Label(header_frame, text="My To-Do List", font=("Helvetica", 24, "bold"), fg="white", bg="#4CAF50")
        header_label.pack()

        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
        input_frame.pack(fill=tk.X)

        self.task_entry = tk.Entry(input_frame, width=30, font=("Helvetica", 14))
        self.task_entry.pack(side=tk.LEFT, padx=(20, 10), pady=10, ipady=5)

        add_button = tk.Button(input_frame, text="➕ Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5)
        add_button.pack(side=tk.LEFT)

        # Tasks Frame
        tasks_frame = tk.Frame(root, bg="#f0f0f0")
        tasks_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        # Scrollbar
        scrollbar = tk.Scrollbar(tasks_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.tasks_listbox = tk.Listbox(tasks_frame, font=("Helvetica", 14), bg="white", bd=0, highlightthickness=0, selectbackground="#4CAF50", activestyle="none", yscrollcommand=scrollbar.set)
        self.tasks_listbox.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.tasks_listbox.yview)

        # Buttons Frame
        buttons_frame = tk.Frame(root, bg="#f0f0f0", pady=10)
        buttons_frame.pack(fill=tk.X)

        mark_done_button = tk.Button(buttons_frame, text="✅ Mark as Done", command=self.mark_done, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5)
        mark_done_button.pack(side=tk.LEFT, padx=10)

        edit_button = tk.Button(buttons_frame, text="✏️ Edit Task", command=self.edit_task, bg="#FF9800", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5)
        edit_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(buttons_frame, text="🗑️ Delete Task", command=self.delete_task, bg="#f44336", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5)
        delete_button.pack(side=tk.LEFT, padx=10)

        clear_done_button = tk.Button(buttons_frame, text="🧹 Clear Completed", command=self.clear_completed, bg="#9E9E9E", fg="white", font=("Helvetica", 12, "bold"), bd=0, padx=10, pady=5)
        clear_done_button.pack(side=tk.LEFT, padx=10)

        # Populate tasks
        self.update_task_listbox()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "status": "Incomplete"})
            self.task_entry.delete(0, tk.END)
            self.update_task_listbox()
            self.save_tasks()
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            display_task = f"{index}. {task['task']} - {task['status']}"
            if task["status"] == "Complete":
                self.tasks_listbox.insert(tk.END, display_task)
                self.tasks_listbox.itemconfig(tk.END, fg="#4CAF50")
            else:
                self.tasks_listbox.insert(tk.END, display_task)

    def mark_done(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            if self.tasks[selected_index]["status"] == "Incomplete":
                self.tasks[selected_index]["status"] = "Complete"
                self.update_task_listbox()
                self.save_tasks()
                messagebox.showinfo("Success", "Task marked as complete!")
            else:
                messagebox.showinfo("Info", "Task is already completed.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def edit_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            current_task = self.tasks[selected_index]["task"]
            new_task = simpledialog.askstring("Edit Task", "Modify the task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_index]["task"] = new_task.strip()
                self.update_task_listbox()
                self.save_tasks()
                messagebox.showinfo("Success", "Task updated successfully!")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    def delete_task(self):
        try:
            selected_index = self.tasks_listbox.curselection()[0]
            confirm = messagebox.askyesno("Delete Confirmation", "Are you sure you want to delete this task?")
            if confirm:
                self.tasks.pop(selected_index)
                self.update_task_listbox()
                self.save_tasks()
                messagebox.showinfo("Success", "Task deleted successfully!")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_completed(self):
        completed_tasks = [task for task in self.tasks if task["status"] == "Complete"]
        if not completed_tasks:
            messagebox.showinfo("Info", "No completed tasks to clear.")
            return
        confirm = messagebox.askyesno("Clear Completed", "Are you sure you want to clear all completed tasks?")
        if confirm:
            self.tasks = [task for task in self.tasks if task["status"] != "Complete"]
            self.update_task_listbox()
            self.save_tasks()
            messagebox.showinfo("Success", "Completed tasks cleared!")

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

