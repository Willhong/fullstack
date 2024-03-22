"use client";
import get from "@/util/util";
import React, { useState } from "react";

const Page = () => {
  const [data, setdata] = useState("");

  const fetchData = async () => {
    const data = await get("https://jsonplaceholder.typicode.com/todos/1");

    setdata(data);
    console.log(data);
  };
  return (
    <>
      <h1>this is about page</h1>
      <h2>this is about page 2</h2>
      <button onClick={fetchData}>fetch data</button>
    </>
  );
};

export default Page;
