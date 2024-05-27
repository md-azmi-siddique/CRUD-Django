// import React from 'react';

import { BrowserRouter, Route, Routes } from "react-router-dom";
import Task from "./pages/Task";
import Update from "./pages/Update";
import Add from "./pages/Add";

const App = () => {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Task/>}/>
          <Route path="/add" element={<Add/>}/>
          <Route path="/update" element={<Update/>}/>
        </Routes>
      </BrowserRouter>
      
    </div>
  );
};

export default App;