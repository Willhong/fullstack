import { Meta, StoryObj } from '@storybook/react'

import label from '../label'

const meta={
    title: 'Label',
    component: label,
    tags: ['autodocs'],
    args:{
        children: 'Hello world!'
        
    }
} satisfies Meta<typeof label>

export default meta
type Story = StoryObj<typeof meta>

export const Default: Story = {
    args:{
        size: 'md',
        color: 'black',
        weight: 'normal'
    }
}
export const SizeVarient: Story = {
    args:{
        size: '4xl',
        
    }
}

export const ColorVarient: Story = {
    args:{
        color: 'red',
    }
}

export const WeightVarient: Story = {
    args:{
        weight: 'bold'
    }
}