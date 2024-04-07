import { Meta, StoryObj } from "@storybook/react";

import button from ".";

const meta = {
  title: "Button",
  component: button,
  tags: ["autodocs"],
  args: {
    children: "Hello world!",
  },
} satisfies Meta<typeof button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = {
  args: {
    variant: "default",
    size: "default",
    outline: false,
    isLoading: false,
    fullWidth: false,
  },
};
