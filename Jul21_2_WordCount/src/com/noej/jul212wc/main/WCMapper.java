package com.noej.jul212wc.main;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// 1단계 : Map

// IN
//		I am a boy
//		You are a girl
//		There is a phone
// OUT
//		I 1
//		am 1
//		a 1
//		boy 1
//		You 1
//		are 1
//		a 1
//		girl 1
//		...
public class WCMapper extends Mapper<Object, Text, Text, IntWritable> {
	// static영역에 하나만 만들어놓고
	private static final Text WORD = new Text();
	private static final IntWritable ONE = new IntWritable(1);
	
	// 한 문장 만날때마다 불러짐
	@Override
	protected void map(
			Object key,	// 데이터가 있나 검사하는 용도
			Text value, // 그 문장(I am a boy.)
			Mapper<Object, Text, Text, IntWritable>.Context context) // 결과처리
			throws IOException, InterruptedException {
		
		String line = value.toString();	// Text -> String
		// split : 정형
		// StringTokenizer : 비정형
		StringTokenizer st = new StringTokenizer(line, " ");
		
		while (st.hasMoreTokens()) {
			// String -> Text
			WORD.set(st.nextToken()); // 값만 바꿔서
			// int -> IntWritable
			context.write(WORD, ONE); // 다음단계로 전송
		}
	}
}
