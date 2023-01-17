import React,{useState, useEffect} from 'react'
import { VscCheckAll } from "react-icons/vsc";

const TodoList = () => {
    const [todos, setTodos] = useState([])

    const style={
        color : "blue"
    }

    useEffect(()=>{
        getTodos()
    },[])

    let getTodos = async ()=>{

        let response = await fetch("http://127.0.0.1:8000/api/todo-list/")
        let data = await response.json()
        console.log(data);
        setTodos(data)
    }

  return (
    <div className="w-full h-3/4 border-2 shadow-lg mt-6">
        <h1 className="bg-slate-700 h-8 text-center my-auto text-white">Your Todos</h1>
        <div>
            {todos?.map(todo=>{
                    <h3 key={todo.id}>{todo.name}</h3>
                    {todo.completed ? <VscCheckAll style={style}/> : <VscCheckAll />}
            }
            )}
        </div>
    </div>
  )
}

export default TodoList