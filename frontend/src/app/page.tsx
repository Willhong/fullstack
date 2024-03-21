"use client";
import ClientHeader from "@/components/ClientHeader";
import { ComboboxDropdownMenu } from "@/components/Dropdown";
import Footer from "@/components/footer";
import Header from "@/components/header";
import Image from "next/image";
import Link from "next/link";
import { useState } from "react";

export default function Home() {
  const [counter, setCounter] = useState(0);

  return (
    <main className="">
      <div className="">
        <h1>this is main page</h1>
        <h2>Get started</h2>
        <div>
          <ComboboxDropdownMenu />
        </div>
        <h3>{counter}</h3>
        <button onClick={() => setCounter(counter + 1)}>Click me</button>
      </div>
    </main>
  );
}
