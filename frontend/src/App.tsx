import { useState } from 'react';
import axios from 'axios';

function App() {
  const [token, setToken] = useState('');
  const [adminMessage, setAdminMessage] = useState('');

  const handleLogin = async () => {
    try {
      const res = await axios.post('/api/login', {
        username: "test_user",
        password: "password"
      });
      setToken(res.data.token);
      setAdminMessage('ログイン成功');
    } catch (error) {
      console.error(error);
    }
  };

  const handleAdminAccess = async () => {
    try {
      const res = await axios.get('/api/admin', {
        headers: { Authorization: `Bearer ${token}` }
      });
      setAdminMessage(res.data.message);
    } catch (error: any) {
      setAdminMessage(error.response?.data?.detail || '通信エラー');
    }
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'sans-serif', maxWidth: '600px' }}>
      <div style={{ marginBottom: '20px', padding: '15px', background: '#f0f0f0' }}>
        <h3>一般ユーザーログイン</h3>
        <button onClick={handleLogin}>ログイン</button>
      </div>
      <div style={{ marginBottom: '20px', padding: '15px', background: '#ffebee' }}>
        <h3>管理者ログイン</h3>
        <button onClick={handleAdminAccess}>ログイン</button>
      </div>
      <div style={{ marginBottom: '20px', padding: '15px', background: '#e0f7fa' }}>
        <h3>JWT</h3>
        <textarea 
          value={token} 
          onChange={(e) => setToken(e.target.value)}
          rows={5} 
          style={{ width: '100%', wordBreak: 'break-all' }}
        />
        <p style={{ fontSize: '12px', color: '#666' }}>
        </p>
        <p>{adminMessage}</p>
      </div>
    </div>
  );
}

export default App;