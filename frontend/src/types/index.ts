export interface Message {
  id: string
  type: 'user' | 'assistant'
  content: string
  timestamp: number
}

export interface StreamEvent {
  type: 'status' | 'token' | 'end' | 'error'
  content: string
  meta?: {
    node?: string
    timestamp?: number
  }
}
