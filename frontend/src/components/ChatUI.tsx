import { useState, useRef, useEffect } from 'react'
import { useChat } from '../hooks/useChat'
import './ChatUI.css'

export default function ChatUI() {
  const { messages, isLoading, sendMessage } = useChat()
  const [input, setInput] = useState('')
  const messagesEndRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages])

  const handleSend = async () => {
    if (!input.trim() || isLoading) return
    await sendMessage(input)
    setInput('')
  }

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>Smart Documentation Agent</h1>
      </div>

      <div className="messages-container">
        {messages.length === 0 ? (
          <div className="empty-state">
            <p>Start a conversation by asking a question</p>
          </div>
        ) : (
          <>
            {messages.map(msg => (
              <div key={msg.id} className={`message message-${msg.type}`}>
                <div className="message-avatar">
                  {msg.type === 'user' ? '👤' : '🤖'}
                </div>
                <div className="message-content">
                  <p>{msg.content}</p>
                </div>
              </div>
            ))}
            <div ref={messagesEndRef} />
          </>
        )}
        {isLoading && (
          <div className="loading">
            <span className="spinner"></span>
            Processing...
          </div>
        )}
      </div>

      <div className="input-container">
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Ask me anything..."
          disabled={isLoading}
          className="chat-input"
        />
        <button
          onClick={handleSend}
          disabled={isLoading || !input.trim()}
          className="send-button"
        >
          Send
        </button>
      </div>
    </div>
  )
}
