
import React, { useRef } from "react";

function NewIdea(props) { 
    const autorInputRef = useRef('testautor');
    const titleInputRef = useRef();
    const rubricsInputRef = useRef();
    const previewInputRef = useRef();
    const bodyInputRef = useRef();
 

    function handleSubmit(e){
        const data = {
            // autor: autorInputRef.current.value,
            autor: 'testautor',
            title: titleInputRef.current.value,
            rubrics: rubricsInputRef.current.value,
            preview: previewInputRef.current.value,
            body: bodyInputRef.current.value,
        }
        console.log(data)
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
                                    <label for="ideaName" className="form-label">Название идеи</label>
                                    <input name="title" ref={titleInputRef} type="text" className="form-control" id="ideaName" placeholder="Название"/>
                                </div>

                                <div className="col">
                                    <label for="" className="form-label">Рубрика</label>
                                    <select className="form-select form-select" name="rubrics" ref={rubricsInputRef} id="">
                                        <option selected value="Python">Python</option>
                                        <option value="JS">JS</option>
                                        <option value="Ещё что-то">Ещё что-то</option>
                                    </select>
                                </div>
                            </div>

                            <div className="row justify-content-center align-items-center g-2">
                                <div className="col">
                                    <label for="preview" className="form-label">Описание</label>
                                    <textarea name="preview"  ref={previewInputRef} type="text" className="form-control" id="preview"
                                        placeholder="Введите описание"></textarea>
                                </div>
                            </div>

                            <div className="row justify-content-center align-items-center g-2 mb-3">
                                <label for="preview" className="form-label">Содержание</label>
                                <textarea name="body" ref={previewInputRef} type="text" className="form-control" id="preview"
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