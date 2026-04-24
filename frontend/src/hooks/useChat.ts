import { useState, useCallback } from 'react'
import { Message } from '../types'

export const useChat = () => {
  const [messages, setMessages] = useState<Message[]>([])
  const [isLoading, setIsLoading] = useState(false)

  const addMessage = useCallback((message: Message) => {
    setMessages(prev => [...prev, message])
  }, [])

  const updateLastMessage = useCallback((content: string) => {
    setMessages(prev => {
      const updated = [...prev]
      if (updated.length > 0) {
        updated[updated.length - 1] = {
          ...updated[updated.length - 1],
          content: updated[updated.length - 1].content + content
        }
      }
      return updated
    })
  }, [])

  const sendMessage = useCallback(async (question: string) => {
    if (!question.trim()) return

    // Add user message
    const userMessage: Message = {
      id: `msg-${Date.now()}`,
      type: 'user',
      content: question,
      timestamp: Date.now()
    }
    addMessage(userMessage)

    // Add assistant placeholder
    const assistantMessage: Message = {
      id: `msg-${Date.now() + 1}`,
      type: 'assistant',
      content: '',
      timestamp: Date.now()
    }
    addMessage(assistantMessage)

    setIsLoading(true)

    try {
      const response = await fetch('/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ question })
      })

      if (!response.body) throw new Error('No response body')

      const reader = response.body.getReader()
      const decoder = new TextDecoder()

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        const text = decoder.decode(value)
        const lines = text.split('\n').filter(line => line.trim())

        for (const line of lines) {
          try {
            const event = JSON.parse(line)
            if (event.type === 'token' && event.content) {
              updateLastMessage(event.content)
            }
          } catch (e) {
            console.error('Failed to parse event:', e)
          }
        }
      }
    } catch (error) {
      console.error('Chat error:', error)
      updateLastMessage('Error: Failed to get response')
    } finally {
      setIsLoading(false)
    }
  }, [addMessage, updateLastMessage])

  return { messages, isLoading, sendMessage, addMessage }
}
