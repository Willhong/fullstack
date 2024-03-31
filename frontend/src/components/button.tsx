import React from "react";
import { Button } from "../components/ui/button";
import classNames from "classnames";

interface Props extends React.ComponentPropsWithoutRef<typeof Button> {
  /**
   * 버튼의 종류를 설정합니다. (기본값: default)
   */
  variant?:
    | "default"
    | "destructive"
    | "outline"
    | "secondary"
    | "ghost"
    | "link";

  /**
   * 버튼의 크기를 설정합니다. (기본값: default)
   */

  size?: "default" | "sm" | "lg" | "icon";
  /**
   * 버튼의 색상을 설정합니다. (기본값: black)
   */
  color?:
    | "red"
    | "blue"
    | "green"
    | "yellow"
    | "purple"
    | "gray"
    | "black"
    | "white"
    | "transparent";
  /**
   * 버튼의 외곽선을 설정합니다. (기본값: false)
   */
  outline?: boolean;
  /**
   * 버튼의 로딩 상태를 설정합니다. (기본값: false)
   * */

  isLoading?: boolean;

  /**
   * 버튼의 너비를 설정합니다. (기본값: false)
   */
  fullWidth?: boolean;
}

/**
 * 버튼 컴포넌트는 사용자와의 상호작용을 위해 사용합니다.
 */
const button = ({
  variant = "default",
  size = "default",
  color = "black",
  outline = false,
  isLoading = false,
  fullWidth = false,
  children,

  ...props
}: Props) => {
  return (
    <Button
      {...props}
      className={classNames(
        props.className,
        size === "default" && "text-md px-2",
        size === "sm" && "text-sm px-3 py-1",
        size === "lg" && "text-lg px-4 py-2",
        size === "icon" && "h-10 w-10",
        fullWidth && "w-full",
        outline === true
          ? {
              "text-white": true,
              border: true,
              "border-black": color === "black",
              "border-slate-300": color === "gray",
              "border-white": color === "white",
              "border-red-500": color === "red",
              "border-blue-500": color === "blue",
              "border-green-500": color === "green",
              "border-yellow-500": color === "yellow",
              "border-purple-500": color === "purple",
            }
          : {
              "text-white": color === "black",
              "text-black": color === "white",
              "bg-black": color === "black",
              "bg-white": color === "white",
              "bg-red-500": color === "red",
              "bg-blue-500": color === "blue",
              "bg-green-500": color === "green",
              "bg-yellow-500": color === "yellow",
              "bg-purple-500": color === "purple",
              "bg-gray-500": color === "gray",
            }
      )}
    >
      {isLoading ? "로딩중" : children}
    </Button>
  );
};

export default button;
