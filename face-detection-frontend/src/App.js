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


import React, { useState } from "react";

const App = () => {
  const [showCamera, setShowCamera] = useState(false);

  return (
    <div className="bg-black text-white min-h-screen flex flex-col items-center">
      {/* Header */}
      <header className="w-full flex justify-between items-center p-4 border-b border-gray-700">
        <h1 className="text-2xl font-bold">FaceDet</h1>
        <nav>
          <ul className="flex space-x-6">
            <li className="cursor-pointer hover:text-gray-400">Home</li>
          </ul>
        </nav>
      </header>

      {/* Main Content */}
      <div className="flex flex-grow w-full max-w-6xl p-6">
        {/* Left Side - Image */}
        <div className="w-1/2 flex items-center justify-center">
          <img
            src="https://www.shutterstock.com/image-vector/vector-human-artificial-head-dispersion-600nw-2481097795.jpg"
            alt="Face Detection Illustration"
            className="w-350 h-280 rounded-lg"
          />
        </div>

        {/* Right Side - Button and Camera */}
        <div className="flex flex-col items-center justify-center w-1/2">
          {!showCamera ? (
            <>
              <p className="text-center text-lg mb-4">
                Face detection uses Deep Learning Models to identify and track faces in real-time,
                enabling various applications like emotion recognition, security,
                and user interaction.
              </p>
              <button
                onClick={() => setShowCamera(true)}
                className="bg-blue-600 hover:bg-blue-500 text-white py-2 px-4 rounded-lg text-lg"
              >
                Start Emotion Detection
              </button>
            </>
          ) : (
            <>
              <img
                src="http://localhost:5000/video_feed"
                alt="Live Video Stream"
                // className="w-96 h-72 rounded-lg border-2 border-gray-700 mt-4"
                className="w-190 h-102 rounded-lg border-2 border-gray-700 mt-4"
              />
              <button
                onClick={() => setShowCamera(false)}
                className="bg-red-600 hover:bg-red-500 text-white py-2 px-4 rounded-lg text-lg mt-4"
              >
                Stop Emotion Detection
              </button>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;
