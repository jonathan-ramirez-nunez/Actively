import React from 'react';
import HomePage from "./HomePage/HomePage";
import { Routes, Route } from "react-router-dom";


function App() {

    return (
        <Routes>
            <Route path='/' element={<HomePage />}></Route>
        </Routes>
    )
    /* return (
        <div>
            <h1>Hello world!</h1>
        </div>
    ) */
}

export default App;