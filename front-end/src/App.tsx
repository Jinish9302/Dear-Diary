import Navbar from "./components/navbar/Navbar.tsx";
import Footer from "./components/footer/Footer.tsx";
import { Route, Routes } from "react-router-dom";
import Home from "./components/Home/Home.tsx";
import ToDoList from "./components/ToDoList/ToDoList.tsx";
import Diary from "./components/Diary/Diary.tsx";
import { useState } from "react";
import SignInBox from "./components/SignInBox/SignInBox.tsx";
function App() {
  const [boxVisibility, setBoxVisibility] = useState(false);

  return (
    <>
      <Navbar 
        OpenSignInBox={
          () => setBoxVisibility(true)
        }
      />
        <Routes>
          <Route path="/" element={<Home/>} />
          <Route path="/ToDo" element={<ToDoList/>} />
          <Route path="/Diary" element={<Diary/>} />
        </Routes>
        <SignInBox 
          close={() => setBoxVisibility(false)} 
          boxVisibility={boxVisibility}
        />
      <Footer />
    </>
  );
}

export default App;
