import "dotenv/config";
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

const addNumbersTool = {
  type: "function",
  name: "add_numbers",
  description: "Adds two numbers together and returns the sum.",
  parameters: {
    type: "object",
    properties: {
      a: { type: "number", description: "The first number" },
      b: { type: "number", description: "The second number" },
    },
    required: ["a", "b"],
  },
};

function addNumbers(a, b) {
  return a + b;
}

const interaction = await ai.interactions.create({
  model: "gemini-3.1-flash-lite",
  input: "What is 47 plus 89?",
  tools: [addNumbersTool],
});

const fcStep = interaction.steps.find((s) => s.type === "function_call");

if (fcStep) {
  console.log(
    `Model wants to call: ${fcStep.name}(${JSON.stringify(fcStep.arguments)})`,
  );

  const result = addNumbers(fcStep.arguments.a, fcStep.arguments.b);

  const finalInteraction = await ai.interactions.create({
    model: "gemini-3.1-flash-lite",
    input: [
      {
        type: "function_result",
        name: fcStep.name,
        call_id: fcStep.id,
        result: [{ type: "text", text: JSON.stringify(result) }],
      },
    ],
    tools: [addNumbersTool],
    previous_interaction_id: interaction.id,
  });

  console.log(finalInteraction.output_text);
} else {
  console.log(interaction.output_text);
}
