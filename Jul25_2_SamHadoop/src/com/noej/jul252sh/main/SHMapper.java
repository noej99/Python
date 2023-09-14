package com.noej.jul252sh.main;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class SHMapper extends Mapper<Object, Text, Text, IntWritable> {

	private static final Text WHO = new Text();
	private static final IntWritable ONE = new IntWritable();
	
	
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, IntWritable>.Context context)
			throws IOException, InterruptedException {

		StringTokenizer st = new StringTokenizer(value.toString(), " ");
		String word = null;
		while (st.hasMoreTokens()) {
			word = st.nextToken();
			if (word.contains("유비") || word.contains("현덕")) {
				WHO.set("유비");
				context.write(WHO, ONE);
			} else if (word.contains("조조") || word.contains("맹덕")) {
				WHO.set("조조");
				context.write(WHO, ONE);
			} else if (word.contains("손권") || word.contains("중모")) {
				WHO.set("손권");
				context.write(WHO, ONE);
			}
		}
	}
}
