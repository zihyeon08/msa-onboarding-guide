#!/usr/bin/env python3
"""
마크다운 파일의 모든 링크 유효성을 확인하는 스크립트
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse

def find_all_markdown_files(root_dir):
    """프로젝트 루트에서 모든 마크다운 파일 찾기"""
    markdown_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                markdown_files.append(os.path.join(dirpath, filename))
    return sorted(markdown_files)

def extract_links(content):
    """마크다운 콘텐츠에서 모든 링크 추출"""
    # [text](url) 형식의 링크 찾기
    markdown_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    return markdown_links

def is_external_url(url):
    """외부 URL인지 확인"""
    return url.startswith('http://') or url.startswith('https://') or url.startswith('mailto:')

def check_file_exists(base_dir, relative_path):
    """상대 경로의 파일이 존재하는지 확인"""
    # 앵커링크 제거 (#로 시작하는 부분)
    file_path = relative_path.split('#')[0]
    
    if not file_path:  # 앵커링크만 있는 경우
        return True, "anchor_only"
    
    full_path = os.path.join(base_dir, file_path)
    normalized_path = os.path.normpath(full_path)
    
    if os.path.isfile(normalized_path):
        return True, "file_exists"
    else:
        return False, "file_not_found"

def main():
    root_dir = '/Users/haedalprogramming/Desktop/msa-onboarding-guide'
    
    markdown_files = find_all_markdown_files(root_dir)
    
    print("=" * 80)
    print("마크다운 문서 링크 유효성 검사")
    print("=" * 80)
    print(f"\n검사 대상: {len(markdown_files)}개 파일\n")
    
    total_links = 0
    broken_links = []
    external_links = []
    
    for md_file in markdown_files:
        relative_file = os.path.relpath(md_file, root_dir)
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"❌ 파일 읽기 실패: {relative_file} - {e}")
            continue
        
        links = extract_links(content)
        
        if not links:
            continue
        
        print(f"\n📄 {relative_file}")
        print(f"   링크 수: {len(links)}")
        
        file_dir = os.path.dirname(md_file)
        
        for text, url in links:
            total_links += 1
            
            # 외부 링크
            if is_external_url(url):
                external_links.append({
                    'file': relative_file,
                    'text': text,
                    'url': url
                })
                print(f"   ✅ [외부] {url}")
            else:
                # 로컬 파일 링크
                exists, status = check_file_exists(file_dir, url)
                
                if exists:
                    print(f"   ✅ {url}")
                else:
                    broken_links.append({
                        'file': relative_file,
                        'text': text,
                        'url': url,
                        'expected_path': os.path.normpath(os.path.join(file_dir, url.split('#')[0]))
                    })
                    print(f"   ❌ {url} [파일 없음]")
    
    # 결과 요약
    print("\n" + "=" * 80)
    print("검사 결과 요약")
    print("=" * 80)
    print(f"총 링크 수: {total_links}")
    print(f"외부 링크: {len(external_links)}")
    print(f"깨진 링크: {len(broken_links)}")
    
    if broken_links:
        print("\n🚨 깨진 링크 목록:")
        print("-" * 80)
        for item in broken_links:
            print(f"\n파일: {item['file']}")
            print(f"  텍스트: [{item['text']}]")
            print(f"  링크: {item['url']}")
            print(f"  예상 경로: {item['expected_path']}")
    
    if external_links:
        print("\n🌐 외부 링크 목록:")
        print("-" * 80)
        for item in external_links:
            print(f"\n파일: {item['file']}")
            print(f"  텍스트: [{item['text']}]")
            print(f"  URL: {item['url']}")
    
    print("\n" + "=" * 80)
    if len(broken_links) == 0:
        print("✅ 모든 링크가 정상입니다!")
    else:
        print(f"⚠️  {len(broken_links)}개의 깨진 링크를 찾았습니다.")
    print("=" * 80)

if __name__ == '__main__':
    main()
