// import React, { useState } from "react";

// const App = () => {
//   const [showCamera, setShowCamera] = useState(false);

//   return (
//     <div style={{ textAlign: "center", padding: "20px" }}>
//       <h1>Real-Time Emotion Detection</h1>
//       {!showCamera ? (
//         <button
//           onClick={() => setShowCamera(true)}
//           style={{
//             padding: "10px 20px",
//             fontSize: "18px",
//             backgroundColor: "#007bff",
//             color: "white",
//             border: "none",
//             borderRadius: "5px",
//             cursor: "pointer",
//           }}
//         >
//           Click Me to Access the Webcam
//         </button>
//       ) : (
//         <img
//           src="http://localhost:5000/video_feed"
//           alt="Live Video Stream"
//           style={{
//             width: "640px",
//             height: "480px",
//             borderRadius: "10px",
//             border: "2px solid black",
//             marginTop: "20px",
//           }}
//         />
//       )}
//     </div>
//   );
// };

// export default App;


// import React, { useState } from "react";

// const App = () => {
//   const [showCamera, setShowCamera] = useState(false);

//   return (
//     <div className="bg-black text-white min-h-screen flex flex-col items-center">
//       {/* Header */}
//       <header className="w-full flex justify-between items-center p-4 border-b border-gray-700">
//         <h1 className="text-2xl font-bold">FaceDet</h1>
//         <nav>
//           <ul className="flex space-x-6">
//             <li className="cursor-pointer hover:text-gray-400">Home</li>
//           </ul>
//         </nav>
//       </header>

//       {/* Main Content */}
//       <div className="flex flex-grow w-full max-w-6xl p-6">
//         {/* Left Side - Image */}
//         <div className="w-1/2 flex items-center justify-center">
//           <img
//             src="https://www.shutterstock.com/image-vector/vector-human-artificial-head-dispersion-600nw-2481097795.jpg"
//             alt="Face Detection Illustration"
//             className="w-350 h-280 rounded-lg"
//           />
//         </div>

//         {/* Right Side - Button and Camera */}
//         <div className="flex flex-col items-center justify-center w-1/2">
//           {!showCamera ? (
//             <>
//               <p className="text-center text-lg mb-4">
//                 Face detection uses Deep Learning Models to identify and track faces in real-time,
//                 enabling various applications like emotion recognition, security,
//                 and user interaction.
//               </p>
//               <button
//                 onClick={() => setShowCamera(true)}
//                 className="bg-blue-600 hover:bg-blue-500 text-white py-2 px-4 rounded-lg text-lg"
//               >
//                 Start Emotion Detection
//               </button>
//             </>
//           ) : (
//             <>
//               <img
//                 src="http://localhost:5000/video_feed"
//                 alt="Live Video Stream"
//                 // className="w-96 h-72 rounded-lg border-2 border-gray-700 mt-4"
//                 className="w-190 h-102 rounded-lg border-2 border-gray-700 mt-4"
//               />
//               <button
//                 onClick={() => setShowCamera(false)}
//                 className="bg-red-600 hover:bg-red-500 text-white py-2 px-4 rounded-lg text-lg mt-4"
//               >
//                 Stop Emotion Detection
//               </button>
//             </>
//           )}
//         </div>
//       </div>
//     </div>
//   );
// };

// export default App;




import { useState } from 'react';
import { Camera, X, Moon, User, BarChart2 } from 'lucide-react';

export default function App() {
  const [cameraActive, setCameraActive] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const startCamera = () => {
    setCameraActive(true);
  };

  const stopCamera = () => {
    setCameraActive(false);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100">
      {/* Header */}
      <header className="bg-gray-800 border-b border-gray-700">
        <div className="container mx-auto px-4">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <h1 className="text-xl font-bold flex items-center">
                  <Moon className="mr-2 text-purple-400" />
                  <span className="text-purple-400">Emotion</span>
                  <span className="text-blue-400">Sense</span>
                  <span className="text-gray-300">AI</span>
                </h1>
              </div>
            </div>
          </div>
        </div>

        {/* Mobile menu */}
        {mobileMenuOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3">
              <a href="#" className="block px-3 py-2 rounded-md text-base font-medium text-white bg-gray-700">Dashboard</a>
              <a href="#" className="block px-3 py-2 rounded-md text-base font-medium text-gray-300 hover:text-white hover:bg-gray-700">Analytics</a>
              <a href="#" className="block px-3 py-2 rounded-md text-base font-medium text-gray-300 hover:text-white hover:bg-gray-700">Documentation</a>
              <a href="#" className="block px-3 py-2 rounded-md text-base font-medium text-gray-300 hover:text-white hover:bg-gray-700">About</a>
            </div>
          </div>
        )}
      </header>

      {/* Main content */}
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          <div className="mb-8">
            <h2 className="text-3xl font-bold mb-2">Face Expression Detection</h2>
            <p className="text-gray-400">
              Detect and analyze facial expressions in real-time using advanced AI technology
            </p>
          </div>

          <div className="bg-gray-800 rounded-xl shadow-xl p-6 border border-gray-700">
            {!cameraActive ? (
              <div className="py-16 flex flex-col items-center text-center">
                <div className="bg-gray-700 p-4 rounded-full mb-6">
                  <Camera size={48} className="text-purple-400" />
                </div>
                <h3 className="text-2xl font-bold mb-4">Ready to Detect Emotions</h3>
                <p className="mb-8 text-gray-400 max-w-md">
                  Our AI can recognize happiness, sadness, anger, surprise, fear, and disgust expressions in real-time
                </p>
                <button
                  onClick={startCamera}
                  className="flex items-center gap-2 bg-gradient-to-r from-purple-500 to-blue-500 hover:from-purple-600 hover:to-blue-600 text-white font-medium py-3 px-8 rounded-lg transition-all shadow-lg hover:shadow-xl"
                >
                  <Camera size={20} />
                  Start Camera
                </button>
              </div>
            ) : (
              <div className="relative">
                <div className="relative flex justify-center">
                  <div className="relative">
                    <img 
                      src="http://localhost:5000/video_feed"
                      alt="Live Emotion Detection"
                      className="rounded-lg border-2 border-gray-600 max-w-full bg-black shadow-xl"
                      style={{ maxHeight: "480px", maxWidth: "640px", minHeight: "320px", minWidth: "480px" }}
                    />
                    <div className="absolute top-4 left-4 bg-gray-800 bg-opacity-75 rounded-lg py-1 px-3 text-sm text-white">
                      Live Detection
                    </div>
                  </div>

                  <button
                    onClick={stopCamera}
                    className="absolute top-2 right-2 bg-red-500 hover:bg-red-600 text-white p-2 rounded-full shadow-md transition-colors"
                    aria-label="Close camera"
                  >
                    <X size={20} />
                  </button>
                </div>

                {/* <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div className="bg-gray-700 rounded-lg p-4 border border-gray-600">
                    <h3 className="font-medium text-gray-200 mb-2 flex items-center">
                      <User className="mr-2 text-purple-400" size={20} />
                      Current Expression
                    </h3>
                    <div className="text-xl font-bold text-white">Neutral</div>
                    <div className="mt-2 h-2 bg-gray-600 rounded-full overflow-hidden">
                      <div className="bg-purple-500 h-2 rounded-full" style={{ width: '40%' }}></div>
                    </div>
                  </div>

                  <div className="bg-gray-700 rounded-lg p-4 border border-gray-600">
                    <h3 className="font-medium text-gray-200 mb-2 flex items-center">
                      <BarChart2 className="mr-2 text-blue-400" size={20} />
                      Emotion Stats
                    </h3>
                    <div className="space-y-2 text-sm">
                      <div className="flex justify-between items-center">
                        <span className="text-gray-300">Happiness</span>
                        <div className="w-2/3 h-1.5 bg-gray-600 rounded-full overflow-hidden">
                          <div className="bg-green-400 h-full rounded-full" style={{ width: '20%' }}></div>
                        </div>
                      </div>
                      <div className="flex justify-between items-center">
                        <span className="text-gray-300">Sadness</span>
                        <div className="w-2/3 h-1.5 bg-gray-600 rounded-full overflow-hidden">
                          <div className="bg-blue-400 h-full rounded-full" style={{ width: '15%' }}></div>
                        </div>
                      </div>
                      <div className="flex justify-between items-center">
                        <span className="text-gray-300">Anger</span>
                        <div className="w-2/3 h-1.5 bg-gray-600 rounded-full overflow-hidden">
                          <div className="bg-red-400 h-full rounded-full" style={{ width: '5%' }}></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div> */}
              </div>
            )}
          </div>

          <div className="mt-8 bg-gray-800 rounded-xl shadow-lg p-6 border border-gray-700">
            <h3 className="text-xl font-bold mb-4">How It Works</h3>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <div className="flex flex-col items-center text-center p-4">
                <div className="bg-purple-900 bg-opacity-50 p-3 rounded-full mb-4">
                  <Camera size={24} className="text-purple-400" />
                </div>
                <h4 className="font-medium mb-2">Capture</h4>
                <p className="text-gray-400 text-sm">
                  Your webcam captures real-time video which is processed locally in your browser
                </p>
              </div>
              <div className="flex flex-col items-center text-center p-4">
                <div className="bg-blue-900 bg-opacity-50 p-3 rounded-full mb-4">
                  <User size={24} className="text-blue-400" />
                </div>
                <h4 className="font-medium mb-2">Analyze</h4>
                <p className="text-gray-400 text-sm">
                  Our AI model identifies facial landmarks and analyzes micro-expressions
                </p>
              </div>
              <div className="flex flex-col items-center text-center p-4">
                <div className="bg-purple-900 bg-opacity-50 p-3 rounded-full mb-4">
                  <BarChart2 size={24} className="text-purple-400" />
                </div>
                <h4 className="font-medium mb-2">Results</h4>
                <p className="text-gray-400 text-sm">
                  View real-time emotional analysis with confidence scores for each expression
                </p>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
