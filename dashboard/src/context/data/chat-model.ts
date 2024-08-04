export enum MessageType {
    text = "text",
}

export interface Message {
    message: string
    sender: string
    time: string
    type: MessageType
}