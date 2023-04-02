
import React, { useRef, useState } from "react";
import axios from "axios";

function NewIdea(props) { 
    const [rubric, setRubric] = useState()
    const titleInputRef = useRef();
    const previewInputRef = useRef();
    const bodyInputRef = useRef();
 

    function handleSubmit(e){
        const autor = JSON.parse(localStorage.getItem('auth'))
        const data = {
            autor: autor.user.username,
            title: titleInputRef.current.value,
            rubrics: rubric,
            preview: previewInputRef.current.value,
            body: bodyInputRef.current.value,
        }
        axios.post("http://127.0.0.1:8000/api/ideas/", data)
    
    
    }
    return (
        <div className="container-md site-container">
            <div className="container-md mt-5">
                <div className="row justify-content-center align-items-top">
                <div className="col-8">
                <div className="mb-3">
                    <form 
                        id="new_idea-form"
                        onSubmit={handleSubmit}>

                        <div className="container">

                            <div className="row justify-content-center align-items-center g-2">
                                
                                <div className="col-8">
                                    <label className="form-label">Название идеи</label>
                                    <input name="title" ref={titleInputRef} type="text" className="form-control" id="ideaName" placeholder="Название"/>
                                </div>

                                <div className="col">
                                    <label className="form-label">Рубрика</label>
                                    <select className="form-select form-select" name="rubrics" value={rubric} onChange={e => { setRubric(e)}} id="">
                                        <option selected value="Python">Python</option>
                                        <option value="JS">JS</option>
                                        <option value="Ещё что-то">Ещё что-то</option>
                                    </select>
                                </div>
                            </div>

                            <div className="row justify-content-center align-items-center g-2">
                                <div className="col">
                                    <label  className="form-label">Описание</label>
                                    <textarea name="preview"  ref={previewInputRef} type="text" className="form-control" id="preview"
                                        placeholder="Введите описание"></textarea>
                                </div>
                            </div>

                            <div className="row justify-content-center align-items-center g-2 mb-3">
                                <label  className="form-label">Содержание</label>
                                <textarea name="body" ref={bodyInputRef} type="text" className="form-control" id="preview"
                                    placeholder="Введите содержание"></textarea>
                            </div>

                            <div className="row justify-content-center align-items-center ">
                                    <button type="submit" className="btn mainButton">Добавить идею</button>
                            </div>

                        </div>
                    </form>
                    
                </div>
                </div>
                </div>
            </div>
        </div>
)};


export default NewIdea