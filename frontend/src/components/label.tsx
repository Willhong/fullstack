import React from "react";
import { Label } from "../components/ui/label";
import classNames from "classnames";

interface Props extends React.ComponentPropsWithoutRef<typeof Label> {
  /**
   * 텍스트의 크기를 설정합니다. (기본값: md)
   */
  size?: "4xl" | "3xl" | "2xl" | "xl" | "lg" | "md" | "sm" | "xs";
  /**
   * 텍스트의 색상을 설정합니다. (기본값: black)
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
   * 텍스트의 굵기를 설정합니다. (기본값: normal)
   */
  weight?: "light" | "normal" | "medium" | "bold";
}

/**
 * 레이블 컴포넌트는 텍스트를 표시할 때 사용합니다.
 */
const label = ({
  size = "md",
  color = "black",
  weight = "normal",
  ...props
}: Props) => {
  return (
    <Label
      {...props}
      className={classNames(
        props.className,
        {
          "text-4xl": size === "4xl",
          "text-3xl": size === "3xl",
          "text-2xl": size === "2xl",
          "text-xl": size === "xl",
          "text-lg": size === "lg",
          "text-md": size === "md",
          "text-sm": size === "sm",
          "text-xs": size === "xs",
        },
        {
          "text-red-500": color === "red",
          "text-blue-500": color === "blue",
          "text-green-500": color === "green",
          "text-yellow-500": color === "yellow",
          "text-purple-500": color === "purple",
          "text-gray-500": color === "gray",
          "text-black": color === "black",
          "text-white": color === "white",
          "text-transparent": color === "transparent",
        },
        {
          "font-light": weight === "light",
          "font-normal": weight === "normal",
          "font-medium": weight === "medium",
          "font-bold": weight === "bold",
        }
      )}
    ></Label>
  );
};

export default label;
