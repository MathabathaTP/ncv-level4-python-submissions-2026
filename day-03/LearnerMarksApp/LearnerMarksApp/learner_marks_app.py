# NCV Level 4 Advanced Python - Learner Marks Management System
# Name: __________________ Student number: __________________
# Date: 19 November 2026
# Description: GUI and console demonstrations of collections, algorithms and learner records.
import json
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog

STARTER = {
    '2024001': {'name':'Thandi','marks':[65,72,58]},
    '2024002': {'name':'Sipho','marks':[48,90,55]},
    '2024003': {'name':'Lerato','marks':[81,39,77]},
    '2024004': {'name':'Dumisani','marks':[72,72,48]},
    '2024005': {'name':'Naledi','marks':[90,55,72]},
}
# A dictionary provides quick access by unique student number.
# Each learner has a list because marks can be appended and duplicates retained.

def total_of(values):
    total = 0
    for value in values: total += value
    return total

def mean_of(values):
    return total_of(values)/len(values) if values else None

def max_of(values):
    if not values: return None
    largest = values[0]
    for value in values[1:]:
        if value > largest: largest = value
    return largest

def min_of(values):
    if not values: return None
    smallest = values[0]
    for value in values[1:]:
        if value < smallest: smallest = value
    return smallest

def range_of(values):
    if not values: return None
    return max_of(values)-min_of(values)

def above_mean(values):
    average = mean_of(values)
    if average is None: return []
    result=[]
    for value in values:
        if value > average: result.append(value)
    return result

def find_first(values,target):
    for i in range(len(values)):
        if values[i] == target: return i
    return -1

def find_all(values,target):
    indices=[]
    for i in range(len(values)):
        if values[i] == target: indices.append(i)
    return indices

def count_of(values,target):
    count=0
    for value in values:
        if value == target: count += 1
    return count

def mode_of(values):
    if not values: return []
    frequencies={}
    for value in values: frequencies[value]=frequencies.get(value,0)+1
    highest=0
    for frequency in frequencies.values():
        if frequency>highest: highest=frequency
    modes=[]
    for value in frequencies:
        if frequencies[value]==highest: modes.append(value)
    return modes

def bubble_sort(values):
    result=values[:]
    for i in range(len(result)-1):
        for j in range(len(result)-1-i):
            if result[j]>result[j+1]: result[j],result[j+1]=result[j+1],result[j]
    return result

def selection_sort(values):
    result=values[:]
    for i in range(len(result)):
        smallest=i
        for j in range(i+1,len(result)):
            if result[j]<result[smallest]: smallest=j
        if smallest!=i: result[i],result[smallest]=result[smallest],result[i]
    return result

def ranking(learners):
    # Descending bubble sort of (average, student number) tuples.
    rows=[]
    for number,record in learners.items():
        avg=mean_of(record['marks'])
        if avg is not None: rows.append((avg,number))
    for i in range(len(rows)-1):
        for j in range(len(rows)-1-i):
            if rows[j][0]<rows[j+1][0]: rows[j],rows[j+1]=rows[j+1],rows[j]
    return rows

def valid_number(number): return len(number)==7 and number.isascii() and number.isdigit()
def valid_mark(mark): return isinstance(mark,int) and not isinstance(mark,bool) and 0<=mark<=100

def run_demonstrations():
    marks=STARTER['2024001']['marks'][:]
    coordinate=(2,4)  # A tuple is suitable because the classroom seat coordinate is fixed.
    row,seat=coordinate
    modules=['ROB401','EDCR401','ROB401','PRG401']
    unique=set(modules)
    data=[65,72,48,90,55,72,48,72]
    lines=['QUESTION 1 - COLLECTIONS',f'List of Thandi marks: {marks}',f'First: {marks[0]} | Last: {marks[-1]} | First two: {marks[:2]}',f'Fixed classroom coordinate: row {row}, seat {seat}',f'Module codes including duplicates: {modules}',f'Unique codes: {len(unique)} | ROB401 is present: {"ROB401" in unique}',
           '\nQUESTION 2 - FIRST-PRINCIPLES ALGORITHMS',f'Data: {data}',f'Total: {total_of(data)} | Mean: {mean_of(data)}',f'Maximum: {max_of(data)} | Minimum: {min_of(data)}',f'Range: {range_of(data)} | Above mean: {above_mean(data)}',
           '\nQUESTION 3 - SEARCH AND MODE',f'First index of 72: {find_first(data,72)}',f'All indices of 72: {find_all(data,72)}',f'Count of 72: {count_of(data,72)}',f'Mode: {mode_of(data)}',f'Tied modes [2,3,2,3,5]: {mode_of([2,3,2,3,5])}',
           '\nQUESTION 4 - SORTING',f'Original: {data}',f'Bubble sort: {bubble_sort(data)}',f'Selection sort: {selection_sort(data)}',f'Original unchanged: {data}', 'Bubble sort swaps adjacent out-of-order values; selection sort finds the smallest remaining value and swaps it into position.']
    return '\n'.join(lines)

def run_tests():
    tests=[('Empty mean',None,mean_of([])),('Empty maximum',None,max_of([])),('Empty minimum',None,min_of([])),('Empty range',None,range_of([])),('Empty modes',[],mode_of([])),('One mark mean',70.0,mean_of([70])),('Repeated marks count',3,count_of([72,72,50,72],72)),('Tied modes',[2,3],mode_of([2,3,2,3,5])),('Missing target',-1,find_first([1,2,3],99)),('Missing learner',False,'9999999' in STARTER),('Total',522,total_of([65,72,48,90,55,72,48,72])),('Mean',65.25,mean_of([65,72,48,90,55,72,48,72])),('First 72 index',1,find_first([65,72,48,90,55,72,48,72],72)),('All 72 indices',[1,5,7],find_all([65,72,48,90,55,72,48,72],72)),('Bubble sort',[48,48,55,65,72,72,72,90],bubble_sort([65,72,48,90,55,72,48,72])),('Selection sort',[48,48,55,65,72,72,72,90],selection_sort([65,72,48,90,55,72,48,72]))]
    lines=['QUESTION 6 - TEST EVIDENCE','Test | Expected | Actual | Result','-'*75]
    for name,expected,actual in tests: lines.append(f'{name} | {expected!r} | {actual!r} | {"PASS" if expected==actual else "FAIL"}')
    lines.append(f'\nPassed: {sum(1 for _,e,a in tests if e==a)}/{len(tests)}')
    return '\n'.join(lines)

class LearnerApp:
    def __init__(self,root):
        self.root=root; root.title('NCV Level 4 | Learner Marks Management System'); root.geometry('1080x720'); root.minsize(800,550)
        self.learners=json.loads(json.dumps(STARTER))
        self.path=Path.home()/'learner_marks_data.json'
        self.load_silent()
        bar=ttk.Frame(root,padding=12); bar.pack(fill='x')
        ttk.Label(bar,text='LEARNER MARKS MANAGEMENT SYSTEM',font=('Arial',17,'bold')).pack(anchor='w')
        ttk.Label(bar,text='NCV Level 4 • Advanced Python • Questions 1–6').pack(anchor='w')
        actions=ttk.Frame(root,padding=(12,0)); actions.pack(fill='x')
        buttons=[('Add learner',self.add_learner),('Find learner',self.find_learner),('Rename',self.rename),('Add mark',self.add_mark),('Delete',self.delete),('Ranking',self.show_ranking),('Q1–Q4 demo',self.demo),('Q6 tests',self.tests),('Save',self.save),('Export report',self.export)]
        for i,(name,action) in enumerate(buttons):
            ttk.Button(actions,text=name,command=action).grid(row=i//5,column=i%5,padx=3,pady=4,sticky='ew')
        for i in range(5): actions.columnconfigure(i,weight=1)
        self.tabs=ttk.Notebook(root); self.tabs.pack(fill='both',expand=True,padx=12,pady=8)
        tableframe=ttk.Frame(self.tabs); self.tabs.add(tableframe,text='Learner records')
        self.tree=ttk.Treeview(tableframe,columns=('number','name','marks','average'),show='headings')
        for key,title,width in [('number','Student number',135),('name','Learner name',220),('marks','Marks',390),('average','Average (%)',130)]:
            self.tree.heading(key,text=title);self.tree.column(key,width=width,anchor='w')
        self.tree.pack(fill='both',expand=True)
        self.output=tk.Text(self.tabs,wrap='word',font=('Consolas',11),padx=12,pady=12)
        self.tabs.add(self.output,text='Demonstrations and test results')
        ttk.Label(root,text='Data saved to your Documents/Home folder on Save. Select a learner row before editing.',padding=(12,0,12,8)).pack(anchor='w')
        self.refresh()
    def load_silent(self):
        if self.path.exists():
            try:
                loaded=json.loads(self.path.read_text(encoding='utf-8'))
                if isinstance(loaded,dict) and all(valid_number(k) and isinstance(v,dict) and isinstance(v.get('name'),str) and v['name'].strip() and isinstance(v.get('marks'),list) and all(valid_mark(m) for m in v['marks']) for k,v in loaded.items()): self.learners=loaded
            except (OSError,ValueError,TypeError): pass
    def refresh(self):
        for item in self.tree.get_children():self.tree.delete(item)
        for number,record in self.learners.items():
            avg=mean_of(record['marks'])
            self.tree.insert('', 'end',iid=number,values=(number,record['name'],', '.join(map(str,record['marks'])),f'{avg:.2f}' if avg is not None else 'No marks'))
    def selected(self):
        selection=self.tree.selection()
        if selection:return selection[0]
        number=simpledialog.askstring('Student number','Enter the 7-digit student number:',parent=self.root)
        if number is None:return None
        if number not in self.learners:messagebox.showwarning('Not found','No learner with that student number.');return None
        return number
    def add_learner(self):
        number=simpledialog.askstring('Add learner','Student number (7 digits):',parent=self.root)
        if number is None:return
        number=number.strip()
        if not valid_number(number):messagebox.showerror('Invalid number','Enter exactly 7 digits.');return
        if number in self.learners:messagebox.showerror('Duplicate','That student number already exists.');return
        name=simpledialog.askstring('Add learner','Learner name:',parent=self.root)
        if name is None:return
        name=name.strip()
        if not name:messagebox.showerror('Invalid name','Name cannot be empty.');return
        text=simpledialog.askstring('Initial marks','Enter marks separated by commas (0–100), or leave blank:',parent=self.root)
        if text is None:return
        marks=[]
        if text.strip():
            for part in text.split(','):
                part=part.strip()
                if not part.isascii() or not part.isdigit() or not valid_mark(int(part)):
                    messagebox.showerror('Invalid marks','Every mark must be a whole number from 0 to 100.');return
                marks.append(int(part))
        self.learners[number]={'name':name,'marks':marks};self.refresh();messagebox.showinfo('Added','Learner added successfully.')
    def find_learner(self):
        number=simpledialog.askstring('Find learner','Student number:',parent=self.root)
        if number is None:return
        number=number.strip()
        if number not in self.learners:messagebox.showinfo('Not found','No learner with that student number.');return
        self.tabs.select(0);self.tree.selection_set(number);self.tree.focus(number);self.tree.see(number)
        r=self.learners[number];messagebox.showinfo('Learner found',f'{number}: {r["name"]}\nMarks: {r["marks"]}')
    def rename(self):
        number=self.selected()
        if not number:return
        name=simpledialog.askstring('Rename learner','New name:',initialvalue=self.learners[number]['name'],parent=self.root)
        if name is None:return
        if not name.strip():messagebox.showerror('Invalid','Name cannot be blank.');return
        self.learners[number]['name']=name.strip();self.refresh()
    def add_mark(self):
        number=self.selected()
        if not number:return
        text=simpledialog.askstring('Add mark','Mark (0–100):',parent=self.root)
        if text is None:return
        text=text.strip()
        if not text.isascii() or not text.isdigit() or not valid_mark(int(text)):
            messagebox.showerror('Invalid','Enter a whole number from 0 to 100.');return
        self.learners[number]['marks'].append(int(text));self.refresh()
    def delete(self):
        number=self.selected()
        if number and messagebox.askyesno('Confirm deletion',f'Delete {self.learners[number]["name"]} ({number})?'):
            del self.learners[number];self.refresh()
    def show_text(self,text):
        self.output.delete('1.0','end');self.output.insert('1.0',text);self.tabs.select(1)
    def show_ranking(self):
        lines=['QUESTION 5 - DESCENDING RANKING','Rank   Number    Name                         Average','-'*65]
        for position,(avg,number) in enumerate(ranking(self.learners),1):
            lines.append(f'{position:<7}{number:<10}{self.learners[number]["name"]:<29}{avg:.2f}%')
        if len(lines)==3:lines.append('No learners have marks yet.')
        self.show_text('\n'.join(lines))
    def demo(self):self.show_text(run_demonstrations())
    def tests(self):self.show_text(run_tests())
    def save(self):
        try:self.path.write_text(json.dumps(self.learners,indent=2),encoding='utf-8');messagebox.showinfo('Saved',f'Data saved to:\n{self.path}')
        except OSError as exc:messagebox.showerror('Save error',str(exc))
    def export(self):
        path=filedialog.asksaveasfilename(defaultextension='.txt',filetypes=[('Text report','*.txt')],initialfile='learner_marks_report.txt')
        if not path:return
        lines=[run_demonstrations(),'\n'+run_tests(),'\nQUESTION 5 - CURRENT LEARNERS AND RANKING']
        for pos,(avg,num) in enumerate(ranking(self.learners),1):lines.append(f'{pos}. {num} - {self.learners[num]["name"]} - {avg:.2f}%')
        lines.append('\nLearners without marks:')
        for num,record in self.learners.items():
            if not record['marks']:lines.append(f'{num} - {record["name"]}')
        try:Path(path).write_text('\n'.join(lines),encoding='utf-8');messagebox.showinfo('Exported',f'Report saved:\n{path}')
        except OSError as exc:messagebox.showerror('Export error',str(exc))

if __name__=='__main__':
    root=tk.Tk()
    LearnerApp(root)
    root.mainloop()
