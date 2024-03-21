// components/ClientHeader.tsx
// This is a new file that you will create for the Client-Specific Header functionality

"use client"; // Important: Add this line to explicitly mark as a Client Component

import { usePathname } from "next/navigation";
import Header from "./header";
import path from "path";

const ClientHeader = () => {
  var pathname = usePathname();
  pathname = pathname.replace("/", "");
  if (pathname === "") {
    pathname = "Home";
  }
  pathname = pathname.charAt(0).toUpperCase() + pathname.slice(1);

  return <Header route={pathname + " - My app"} />;
};

export default ClientHeader;
