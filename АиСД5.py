from dataclasses import dataclass
import random as rd


class Stack:
    def __init__(self):
        self.data = []
        self.empty = True

    def __str__(self):
        out = '['
        for i in range(self.size() - 1):
            out += str(self.data[i])
        return out + ']'

    def push(self, item):
        self.data.append(item)
        if self.empty:
            self.empty = False

    def pop(self):
        if not self.check_empty():
            out = self.data.pop()
        else:
            out = None
        if not self.data:
            self.empty = True
        return out

    def check_empty(self):
        if self.empty:
            return self.empty
        else:
            return self.empty

    def size(self):
        return len(self.data)


class Queue:
    def __init__(self):
        self.data = []
        self.empty = True

    def __str__(self):
        out = '['
        for i in range(self.size() - 1):
            out += str(self.data[i])
        return out + ']'

    def push(self, item):
        self.data.insert(0, item)
        if self.empty:
            self.empty = False

    def pop(self):
        if not self.check_empty():
            out = self.data.pop()
        else:
            out = None
        if not self.data:
            self.empty = True
        return out

    def check_empty(self):
        if self.empty:
            return self.empty
        else:
            return self.empty

    def size(self):
        return len(self.data)


@dataclass()
class TaskData:
    time: int = None
    priority: int = None


class Task:
    def __init__(self, task_priority, task_time):
        self.current_task = TaskData()
        self.current_task.time = task_time
        self.current_task.priority = task_priority

    def __str__(self):
        return '[' + str(self.get_priority()) + ',' + str(self.get_time()) + ']'

    def get_time(self):
        return self.current_task.time

    def get_priority(self):
        return self.current_task.priority


class TaskGenerator:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.queue3 = Queue()

    def __str__(self):
        out = str(self.queue1) + '\n' + str(self.queue2) + '\n' + str(self.queue3)
        return out + '\n'

    def gen_task(self):
        task = Task(rd.randint(1, 3), rd.randint(4, 8))
        if task.get_priority() == 1:
            self.queue1.push(task)
        elif task.get_priority() == 2:
            self.queue2.push(task)
        else:
            self.queue3.push(task)

    def get_task(self):
        if not self.queue1.check_empty():
            task = self.queue1.pop()
        elif not self.queue2.check_empty():
            task = self.queue2.pop()
        elif not self.queue3.check_empty():
            task = self.queue3.pop()
        else:
            task = None
        return task

    def none_task(self):
        return self.queue1.check_empty() and self.queue2.check_empty() and self.queue3.check_empty()


@dataclass()
class Thread:
    work_time: int = None
    task_priority: int = None
    idle: bool = True


class Processor:
    def __init__(self):
        self.thread = Thread()
        self.wait = Stack()

    def __str__(self):
        out = '|thread|type|time|idle |\n'
        out += '{:<9}{:<5}{:<5}{:<6}'.format('  1', str(self.thread.task_priority), str(self.thread.work_time),
                                             str(self.thread.idle)) + '\n'
        return out

    def add_task(self, task: Task):
        if self.thread.idle:
            self.thread.task_priority = task.get_priority()
            self.thread.work_time = task.get_time()
            self.thread.idle = False
        else:
            self.wait.push(task)

    def __run_task_thread(self):
        self.thread.work_time -= 1
        if self.thread.work_time <= 0:
            self.thread.idle = True
            self.thread.task_priority = None
            self.thread.work_time = None

    def running(self):
        if not self.thread.idle:
            self.__run_task_thread()
        else:
            self.thread.idle = True

    def idle_proc(self):
        return self.thread.idle


generator = TaskGenerator()
processor = Processor()

for i in range(50):
    generator.gen_task()

while True:
    task = generator.get_task()
    if not generator.none_task():
        processor.add_task(task)
    elif not processor.wait.check_empty():
        processor.add_task(processor.wait.pop())
    processor.running()
    print('Tasks\n', generator)
    print('Processor:\n', processor)
    print('Stack:', processor.wait)
    if generator.none_task() and processor.wait.check_empty() and processor.idle_proc():
        break
