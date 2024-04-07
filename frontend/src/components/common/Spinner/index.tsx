import React from "react";
import { Button } from "../../ui/button";
import classNames from "classnames";

interface Props {
  /**
   * 스피너의 크기를 설정합니다. (기본값: md)
   *
   **/
  size?: "xs" | "sm" | "md";
}
const Spinner = ({ size = "md" }: Props) => {
  return (
    <span
      className="material-symbols-outlined animate-spin"
      style={{
        fontSize: size === "xs" ? "1rem" : size === "sm" ? "1.5rem" : "2rem",
      }}
    >
      progress_activity
    </span>
  );
};

export default Spinner;
