const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const http = require('http');

let mainWindow;

function checkStreamlitServer(callback) {
  const options = {
    host: 'localhost',
    port: 8501,
    timeout: 2000, // 2 seconds
  };

  const req = http.request(options, (res) => {
    if (res.statusCode === 200) {
      callback(true);
    } else {
      callback(false);
    }
  });

  req.on('error', () => {
    callback(false);
  });

  req.end();
}

function waitForStreamlitServer(callback) {
  const interval = setInterval(() => {
    checkStreamlitServer((isRunning) => {
      if (isRunning) {
        clearInterval(interval);
        callback();
      }
    });
  }, 1000); // Check every second
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      contextIsolation: true,
    },
  });

  mainWindow.loadURL('http://localhost:8501');

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

function startStreamlit() {
  const streamlitProcess = exec('streamlit run Site.py', (error, stdout, stderr) => {
    if (error) {
      console.error(`Streamlit error: ${error.message}`);
      return;
    }
    if (stderr) {
      console.error(`Streamlit stderr: ${stderr}`);
    }
    console.log(`Streamlit stdout: ${stdout}`);
  });

  return streamlitProcess;
}

app.on('ready', () => {
  const streamlitProcess = startStreamlit();
  waitForStreamlitServer(() => {
    createWindow();
  });

  // Ensure Streamlit process stops when the app quits
  app.on('quit', () => {
    streamlitProcess.kill();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
